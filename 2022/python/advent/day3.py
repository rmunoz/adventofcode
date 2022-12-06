"""
https://adventofcode.com/2022/day/3
"""
from io import TextIOBase
import sys


def priority(item: str) -> int:
    if ord(item) >= ord("a"):
        return ord(item) - ord("a") + 1

    return ord(item) - ord("A") + 27


def calculate_priority(rucksack: str) -> int:
    pos = int(len(rucksack)/2)

    return sum([priority(item) for item in set(rucksack[:pos]) & set(rucksack[pos:])])


def check_rucksacks(data: TextIOBase) -> int:
    return sum([calculate_priority(line) for line in data.read().splitlines()])


def check_badges(data: TextIOBase) -> int:
    rucksacks = data.read().splitlines()

    accum = 0
    for i in range(0, len(rucksacks), 3):
        a, b, c = rucksacks[i:i+3]
        accum += sum([priority(item) for item in set(a) & set(b) & set(c)])

    return accum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        sys.exit(-1)

    with open(sys.argv[1], "r", encoding="utf-8") as fhandle:
        print(f"priority sum: {check_rucksacks(fhandle)}")

    with open(sys.argv[1], "r", encoding="utf-8") as fhandle:
        print(f"badges sum: {check_badges(fhandle)}")
