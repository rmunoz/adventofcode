from io import StringIO

import pytest

from advent.day4 import camp_cleanup_overlap_count, camp_cleanup_contained_count


@pytest.fixture(name="elves_input")
def elves_input_fixture() -> StringIO:
    return StringIO(
        r"""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
    )


def test_contained_count(elves_input: StringIO) -> None:
    assert camp_cleanup_contained_count(elves_input) == 2

def test_overlap_count(elves_input: StringIO) -> None:
    assert camp_cleanup_overlap_count(elves_input) == 4
