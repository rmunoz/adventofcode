"""
https://adventofcode.com/2022/day/7
"""
from __future__ import annotations

from dataclasses import dataclass, field
from io import TextIOBase
import sys
from typing import Tuple

TOTAL_DISK_SIZE = 70000000
UPDATE_SIZE = 30000000


@dataclass
class Inode:
    """Class for representing a filesystem inode"""
    name: str
    size: int = 0
    inodes: list[Inode] = field(default_factory=list)

    def __str__(self) -> str:
        return f"'{self.name}' ({'dir' if self.inodes else 'file'}, size={self.size})"


def pretty_print(inode: Inode, depth: int = 0) -> None:
    print("  " * depth + "- " + str(inode))
    for item in inode.inodes:
        pretty_print(item, depth=depth+1)


def update_directory_sizes(inode: Inode, dirs: list[Inode]) -> int:
    """Traverses inode and childs updating dir sizes and populating dirs list with just dir inode type"""
    if inode.inodes:
        inode.size = sum(update_directory_sizes(item, dirs) for item in inode.inodes)
        dirs.append(inode)

    return inode.size


def process_filesystem(data: TextIOBase, max_size: int = 100000) -> Tuple[int, int]:
    tree = Inode("/")
    traverse_stack: list[Inode] = [tree]

    for line in data.read().splitlines():
        items = line.split(" ")
        if items[0] == "$":  # is a command
            if items[1] == "cd":
                if items[2] == "..":
                    traverse_stack.pop()
                else:
                    for inode in traverse_stack[-1].inodes:
                        if items[2] == inode.name:
                            traverse_stack.append(inode)
                            break
        else:  # is a ls output
            if items[0] == "dir":
                traverse_stack[-1].inodes.append(Inode(name=items[1]))
            else:
                traverse_stack[-1].inodes.append(
                    Inode(name=items[1], size=int(items[0])))

    dirs: list[Inode] = []
    update_directory_sizes(tree, dirs)
    dirs.sort(key=lambda i: i.size)

    unused_space = TOTAL_DISK_SIZE - dirs[-1].size
    min_space_required = UPDATE_SIZE - unused_space
    for directory in dirs:
        if directory.size >= min_space_required:
            break

    return sum([dir.size for dir in dirs if dir.size <= max_size]), directory.size


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        sys.exit(-1)

    with open(sys.argv[1], "r", encoding="utf-8") as fhandle:
        min_dirs_sum, dir_size_to_delete = process_filesystem(fhandle)
        print(f"{min_dirs_sum=} {dir_size_to_delete=}")
