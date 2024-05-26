# type: ignore

from typing import Any

import requests
from bs4 import BeautifulSoup


def scrape_problem(url: str) -> dict[str, Any]:
    response = requests.get(url)
    soup = (
        BeautifulSoup(response.text, "html.parser")
        .find("div", {"id": "task-statement"})
        .find("span", class_="lang-en")
    )

    problem = {}

    # 問題文
    problem_statement_section = soup.find("h3", string="Problem Statement").find_next_sibling("p")
    problem_statement = problem_statement_section.get_text(" ", strip=True)
    problem["Problem Statement"] = problem_statement

    # 制約
    constraints_section = soup.find("h3", string="Constraints").find_next_sibling("ul")
    constraints = constraints_section.get_text(" ", strip=True)
    problem["Constraints"] = constraints

    # 入力
    input_section = soup.find("h3", string="Input").find_next_sibling("p")
    input_explantaion = input_section.get_text(" ", strip=True)
    input_format = input_section.find_next_sibling("pre").get_text(" ", strip=True)
    problem["Input"] = {"Explanation": input_explantaion, "Format": input_format}
    # 出力
    output_section = soup.find("h3", string="Output").find_next_sibling("p")
    output = output_section.get_text(" ", strip=True)
    problem["Output"] = output

    # サンプルケース
    sample_input_sections = soup.find_all(
        "h3", string=lambda text: text and text.startswith("Sample Input")
    )
    sample_output_sections = soup.find_all(
        "h3", string=lambda text: text and text.startswith("Sample Output")
    )

    for sample_id, (input_section, output_section) in enumerate(
        zip(sample_input_sections, sample_output_sections)
    ):
        sample_input = input_section.find_next_sibling("pre").get_text(" ", strip=True)
        sample_output = output_section.find_next_sibling("pre").get_text(" ", strip=True)
        explanation = output_section.find_next_sibling("p")
        explanation_text = explanation.get_text(" ", strip=True) if explanation else ""
        problem[f"Sample_Case_{sample_id}"] = {
            "Input": sample_input,
            "Output": sample_output,
            "Explanation": explanation_text,
        }

    return problem
