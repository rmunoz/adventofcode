from io import StringIO

import pytest

from advent.day3 import check_badges, check_rucksacks, priority


@pytest.fixture(name="elves_input")
def elves_input_fixture() -> StringIO:
    return StringIO(
        r"""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
    )


def test_priotity() -> None:
    for item, expected in zip(["p", "L", "P", "v", "t", "s"], [16, 38, 42, 22, 20, 19]):
        assert priority(item) == expected


def test_check_rucksacks(elves_input: StringIO) -> None:
    assert check_rucksacks(elves_input) == 157


def test_badges(elves_input: StringIO) -> None:
    assert check_badges(elves_input) == 70
