from io import StringIO

import pytest

from advent.day2 import Strategy, compute_score


@pytest.fixture(name="fx_in")
def input_fixture() -> StringIO:
    return StringIO(
        r"""A Y
B X
C Z
"""
    )


def test_what_to_play_strategy(fx_in: StringIO) -> None:
    assert compute_score(fx_in, Strategy.WHAT_TO_PLAY) == 15


def test_match_result_strategy(fx_in: StringIO) -> None:
    assert compute_score(fx_in, Strategy.MATCH_RESULT) == 12
