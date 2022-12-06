"""
https://adventofcode.com/2022/day/4
"""
from __future__ import annotations

from dataclasses import dataclass
from io import TextIOBase
import sys
from typing import Tuple


@dataclass
class Assignment:
    start: int
    end: int

    def is_contained(self, other: Assignment) -> bool:
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: Assignment) -> bool:
        return ((other.start >= self.start and other.start <= self.end) or
                (other.end >= self.start and other.end <= self.end))


def get_sets(line: str) -> Tuple[Assignment, Assignment]:
    first, second = line.split(",")
    fstart, fend = first.split("-")
    sstart, send = second.split("-")

    return Assignment(int(fstart), int(fend)), Assignment(int(sstart), int(send))


def camp_cleanup_contained_count(data: TextIOBase) -> int:
    accum = 0
    for line in data.read().splitlines():
        a, b = get_sets(line)
        if a.is_contained(b) or b.is_contained(a):
            accum += 1

    return accum


def camp_cleanup_overlap_count(data: TextIOBase) -> int:
    accum = 0
    for line in data.read().splitlines():
        a, b = get_sets(line)
        if a.overlaps(b) or b.overlaps(a):
            accum += 1

    return accum


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        sys.exit(-1)

    with open(sys.argv[1], "r", encoding="utf-8") as fhandle:
        print(f"contained: {camp_cleanup_contained_count(fhandle)}")

    with open(sys.argv[1], "r", encoding="utf-8") as fhandle:
        print(f"overlaps: {camp_cleanup_overlap_count(fhandle)}")
