from io import StringIO

import pytest

from advent.day1 import calorie_counting


@pytest.fixture(name="elves_input")
def elves_input_fixture() -> StringIO:
    return StringIO(
        r"""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
    )


def test_calorie_counting_first(elves_input: StringIO) -> None:
    assert calorie_counting(elves_input) == 24000


def test_calorie_counting_first_three(elves_input: StringIO) -> None:
    assert calorie_counting(elves_input, 3) == 45000
