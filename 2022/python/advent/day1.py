"""
https://adventofcode.com/2022/day/1
"""
from io import TextIOBase
import sys


def calorie_counting(data: TextIOBase, first_n: int = 1) -> int:
    """
    Reads elves calories file and returns the maximun calories carried by an elf
    """
    cals = []
    accum = 0
    for line in data:
        if line != "\n":
            accum += int(line)
        else:
            cals.append(accum)
            accum = 0

    if accum:
        cals.append(accum)

    cals.sort(reverse=True)

    return sum(cals[:first_n])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} input_file elves")
        sys.exit(-1)

    with open(sys.argv[1], "r", encoding="utf-8") as fhandle:
        print(f"calorie counting: {calorie_counting(fhandle, int(sys.argv[2]))}")
