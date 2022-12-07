from io import StringIO

import pytest

from advent.day7 import process_filesystem


@pytest.fixture(name="elves_input")
def elves_input_fixture() -> StringIO:
    return StringIO(
        r"""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
    )


def test_process_filesystem(elves_input: StringIO) -> None:
    assert process_filesystem(elves_input) == (95437, 24933642)
