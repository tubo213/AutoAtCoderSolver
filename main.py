import json
import os
import subprocess
import time

import click
from loguru import logger

from src.solver import GPTSolver


def download_contest(contest_id: str) -> None:
    # atcoder cliでコンテストをダウンロード
    subprocess.run(["acc", "new", contest_id, "-c", "all"])


def load_contest() -> dict:
    # コンテストの情報を取得
    with open("contest.acc.json", "r") as f:
        contest = json.load(f)
    return contest


@click.command()
@click.argument("contest_id", type=str)
@click.option("--choice", "-c", type=str, default="all")
@click.option("--n_trials", "-n", type=int, default=5)
@click.option("--model", "-m", type=str, default="gpt-4o")
@click.option("interval", "-i", type=float, default=5.0)
def main(contest_id: str, choice: str, n_trials: int, model: str, interval: float) -> None:
    # contestsディレクトリに移動
    os.chdir("contests")

    # コンテストをダウンロード
    if not os.path.exists(contest_id):
        download_contest(contest_id)
    # contest_idのディレクトリに移動
    os.chdir(contest_id)

    # コンテストの情報を取得
    contest = load_contest()

    # GPTSolverで問題を並列で解く
    solver = GPTSolver(model=model, n_trials=n_trials)
    for task in contest["tasks"]:
        # choiceが指定されている場合はその問題だけを解く
        if choice == "all":
            pass
        elif choice == task["label"]:
            pass
        else:
            continue

        # 問題を解く
        t0 = time.time()
        try:
            result = solver.solve(task)
            if result != 0:
                logger.error(f"Failed to solve {task['label']}")
            else:
                logger.success(f"Solved {task['label']}!")
        except Exception as e:
            logger.error(f"Failed to solve {task['label']}: {e}")
            continue
        t1 = time.time()

        # interval秒待つ
        interval = max(0.0, interval - (t1 - t0))
        logger.info(f"Sleeping {interval} seconds...")
        time.sleep(interval)


if __name__ == "__main__":
    main()
