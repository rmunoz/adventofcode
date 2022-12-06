"""
https://adventofcode.com/2022/day/2
"""
from enum import IntEnum
from io import TextIOBase
import sys

_compute_score_map = {
    ("A", "A"): 4,
    ("A", "B"): 8,
    ("A", "C"): 3,
    ("B", "A"): 1,
    ("B", "B"): 5,
    ("B", "C"): 9,
    ("C", "A"): 7,
    ("C", "B"): 2,
    ("C", "C"): 6,
}


class Strategy(IntEnum):
    """The strategy to use"""

    WHAT_TO_PLAY = 1
    MATCH_RESULT = 2

    def choice(self, me: str, opponent: str) -> str:
        return {
            ("X", None): "A",
            ("Y", None): "B",
            ("Z", None): "C",
            ("X", "A"): "C",
            ("X", "B"): "A",
            ("X", "C"): "B",
            ("Y", "A"): "A",
            ("Y", "B"): "B",
            ("Y", "C"): "C",
            ("Z", "A"): "B",
            ("Z", "B"): "C",
            ("Z", "C"): "A",
        }[(me, None if self == Strategy.WHAT_TO_PLAY else opponent)]


def compute_score(data: TextIOBase, strategy: Strategy) -> int:
    """Computes stragegy score"""
    score = 0
    for line in data:
        opponent, me = line.rstrip().split(" ")
        score += _compute_score_map[(opponent, strategy.choice(me, opponent))]

    return score


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} input_file strategy (1: for should_play or 2: for result)")
        sys.exit(-1)

    with open(sys.argv[1], "r", encoding="utf-8") as fhandle:
        print(f"calorie counting: {compute_score(fhandle, Strategy(int(sys.argv[2])))}")
