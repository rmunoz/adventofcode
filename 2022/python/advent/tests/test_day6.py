from typing import Tuple

import pytest

from advent.day6 import get_start_of_message, get_start_of_packet

elves_input = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26)
]


@pytest.mark.parametrize("elves_input_row", elves_input)
def test_start_of(elves_input_row: Tuple[str, int, int]) -> None:
    signal, start_of_packet_pos, start_of_message_pos = elves_input_row
    assert get_start_of_packet(signal) == start_of_packet_pos
    assert get_start_of_message(signal) == start_of_message_pos
