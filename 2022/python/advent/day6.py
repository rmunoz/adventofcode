"""
https://adventofcode.com/2022/day/6
"""
from pathlib import Path
import sys


def get_n_distinct_pos(signal: str, window_size: int) -> int:
    for begin, _ in enumerate(signal):
        end = begin + window_size
        if len(set(signal[begin:end])) == window_size:
            return end

    return len(signal)

def get_start_of_packet(signal: str) -> int:
    return get_n_distinct_pos(signal, 4)

def get_start_of_message(signal: str) -> int:
    return get_n_distinct_pos(signal, 14)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        sys.exit(-1)

    print(f"start-of-packet: {get_start_of_packet(Path(sys.argv[1]).read_text())}")
    print(f"start-of-message: {get_start_of_message(Path(sys.argv[1]).read_text())}")
