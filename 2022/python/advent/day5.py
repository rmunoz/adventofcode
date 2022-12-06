"""
https://adventofcode.com/2022/day/3
"""
from io import TextIOBase
import sys
from typing import Tuple

SupplyType = list[str]
RulesType = list[Tuple[int, ...]]


def build_data_structures(data: TextIOBase) -> Tuple[SupplyType, RulesType]:
    supply: SupplyType = []
    rules: RulesType = []

    process_rules = False
    for line in data.read().splitlines():
        if line == "":
            process_rules = True
            continue

        if "[" in line:
            line += " "
            for pos, i in enumerate(range(0, len(line), 4)):
                if len(supply) <= pos:
                    supply.append("")

                supply[pos] += line[i:i+4].strip().replace('[', '').replace(']', '')

        if process_rules:
            items = [int(item) for item in line.split(" ") if item.isdigit()]
            # prepare the tuple for processing: first element negative, second and third are zero based
            # positions in the array
            rules.append((int(items[0]) * -1, int(items[1]) - 1, int(items[2]) - 1))

    return [i[::-1] for i in supply], rules


def rearrange_stacks(data: TextIOBase, reverse: bool = True) -> str:
    supply, rules = build_data_structures(data)

    for remove_count, src, dest in rules:
        remainder_count = len(supply[src]) + remove_count  #  remove_count is negatives so its substracting
        supply[src], to_move = supply[src][:remainder_count], supply[src][remove_count:]
        supply[dest] += to_move[::-1] if reverse else to_move

    return "".join([line[-1] for line in supply])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input_file")
        sys.exit(-1)

    with open(sys.argv[1], "r", encoding="utf-8") as fhandle:
        print(f"top stacks reversed: {rearrange_stacks(fhandle)}")

    with open(sys.argv[1], "r", encoding="utf-8") as fhandle:
        print(f"top stacks: {rearrange_stacks(fhandle, reverse=False)}")
