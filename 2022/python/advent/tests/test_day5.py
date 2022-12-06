from io import StringIO

import pytest

from advent.day5 import build_data_structures, rearrange_stacks


@pytest.fixture(name="elves_input")
def elves_input_fixture() -> StringIO:
    return StringIO(r"""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""")


def test_build_data_structures(elves_input: StringIO) -> None:
    supply, rules = build_data_structures(elves_input)
    assert supply == ["ZN", "MCD", "P"]
    assert rules == [(-1, 1, 0), (-3, 0, 2), (-2, 1, 0), (-1, 0, 1)]


def test_rearrange_stacks_reverse(elves_input: StringIO) -> None:
    assert rearrange_stacks(elves_input) == "CMZ"

def test_rearrange_stacks(elves_input: StringIO) -> None:
    assert rearrange_stacks(elves_input, reverse=False) == "MCD"
