import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

import openai
from dotenv import load_dotenv
from loguru import logger

from src.scraper import scrape_problem

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]


class GPTSolver:
    SYSTEM_PROMPT = """
        You are a highly skilled competitive programmer. Please write efficient and correct code in Python to solve the given problem. Follow these detailed steps to ensure the solution meets the requirements:

        1. **Understand the Problem:**
           - Carefully read the problem statement and constraints.
           - Identify the type of problem and the best approach to solve it (e.g., dynamic programming, graph algorithms, greedy algorithms).

        2. **Plan the Solution:**
           - Explain your thought process and the steps needed to solve the problem.
           - Clearly define the computational complexity of your approach.
           - Consider the constraints and ensure the solution is efficient.
           - Identify potential edge cases and plan how to handle them.

        3. **Write the Code:**
           - Implement the solution in Python, ensuring it is executable with `python main.py` when standard input is provided.
           - Combine the entire solution into a single code block.
           - Include comments to explain the key parts of your code.
           - Optimize the code to ensure the execution time is within 2 seconds and the memory usage is within 1024 MB.
           - if __name__ == "__main__":; main() is must be included.

        The problem description will be given in JSON format as follows:

        {
            "Problem Statement": "<problem_description>",
            "Constraints": "<constraints>",
            "Input": {
                "Explanation": "<input_description>",
                "Format": "<input_format>",
            },
            "Output": "<output_description>",
            "Sample_Case_0": {
                "Input": "<input_0>",
                "Output": "<output_0>",
                "Explanation": "<explanation_0>"
            },
            "Sample_Case_1": {
                "Input": "<input_1>",
                "Output": "<output_1>",
                "Explanation": "<explanation_1>"
            },
            ...
        }

        Example:

        {
            "Problem Statement": "Takahashi's cake has been eaten by someone. There are three suspects: person 1 , person 2 , and person 3 .",
            "Constraints": "1 \\leq A, B \\leq 3 All input values are integers.",
            "Input": {
                "Explanation": "The input is given from Standard Input in the following format:",
                "Format": "A B"
            },
            "Output": "If the culprit can be uniquely identified based on the memories of the two witnesses, print the person's number; otherwise, print -1 .",
            "Sample_Case_0": {
                "Input": "1 2",
                "Output": "3",
                "Explanation": "From the memories of the two witnesses, it can be determined that person 3 is the culprit."
            },
            "Sample_Case_1": {
                "Input": "1 1",
                "Output": "-1",
                "Explanation": "From the memories of the two witnesses, it cannot be determined whether person 2 or person 3 is the culprit. Therefore, print -1 ."
            }
        }
    """
    IMPROVEMENT_PROMPT = """
        You previously wrote the following code to solve the given problem:

        ```
        {code}
        ```

        However, the code did not pass all the test cases. Here are the results of the test cases:

        ```
        {result}
        ```

        Please carefully analyze the failed test cases and identify the reasons for the failures. Consider the following steps to improve your code:

        1. **Analyze Test Case Failures:**
        - Identify which test cases failed and understand why they failed.
        - Check if there are logical errors, edge cases not handled, or performance issues.

        2. **Improve the Code:**
        - Fix the identified issues in the code.
        - Ensure that the code meets the problem's requirements and constraints.
        - Consider optimizing the code for better performance if needed.

        Provide the improved code in a single code block.
    """

    def __init__(self, model: str = "gpt-4o", n_trials: int = 5) -> None:
        self.model = model
        self.n_trials = n_trials

    def solve(self, task: dict[str, Any]) -> int:
        logger.info(f"Solving {task['label']}...")
        problem = scrape_problem(task["url"])
        messages: list[Any] = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(problem)},
        ]

        # n_trials回までリトライする
        trial = 0
        while trial < self.n_trials:
            solution = openai.chat.completions.create(
                model=self.model, messages=messages, max_tokens=1000
            )
            content = solution.choices[0].message.content
            code = extract_code_block(content)  # type: ignore

            # 回答をresponseに書き込む
            content_path = Path(task["directory"]["path"]) / f"content{trial}.txt"
            with open(content_path, "w") as f:
                f.write(content)  # type: ignore

            # コードをファイルに書き込む
            file_path = Path(task["directory"]["path"]) / "main.py"
            with open(file_path, "w") as f:
                f.write(code)
            # ruffでformat
            subprocess.run(["ruff", "format"])

            # ojでテストケースを実行
            test_dir = Path(task["directory"]["path"]) / "test"
            result = subprocess.run(
                ["oj", "t", "-c", f"python {file_path}", "-d", test_dir], capture_output=True
            )

            # テストケースが通ったら提出して終了
            if result.returncode == 0:
                logger.success("The code passed all test cases!")
                subprocess.run(
                    ["oj", "s", task["url"], file_path, "-y", "--guess-python-interpreter", "pypy"]
                )
                return 0
            else:
                # テストケースが通らなかったら、結果を表示してリトライ
                case_results = result.stdout.decode()
                messages.append(
                    {
                        "role": "system",
                        "content": self.IMPROVEMENT_PROMPT.format(code=code, result=case_results),
                    }
                )
                logger.error(f"Trial {trial + 1} failed! Retrying...")
                logger.info(f"Case Results:\n{case_results}")
                # main.pyをerror.pyにリネーム
                error_path = Path(task["directory"]["path"]) / "error.py"
                file_path.rename(error_path)
                trial += 1

        logger.error(f"Failed to solve {task['label']} after {self.n_trials} trials.")
        return 1


def extract_code_block(text: str) -> str:
    """
    Extract code blocks from a given text, ignoring language specifiers.

    Args:
        text (str): The input text containing code blocks.

    Returns:
        list: A list of extracted code blocks.
    """
    # Regular expression to match code blocks enclosed in triple backticks
    # and optionally preceded by a language specifier
    code_block_pattern = re.compile(r"```(?:\w+)?\n(.*?)```", re.DOTALL)

    # Find all matches of the code block pattern
    code_blocks: list[str] = code_block_pattern.findall(text)

    return code_blocks[0]
