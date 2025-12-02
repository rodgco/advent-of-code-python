# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import IntSplit2RowSolution, answer
from ...utils.text_utils import split_into_chunks
from ...utils.arr_utils import all_equal

class Solution(IntSplit2RowSolution):
    _year = 2025
    _day = 2

    separator = ","
    separator2 = "-"

    # @answer(1234)
    def part_1(self) -> int:
        count = 0
        for rng in self.input:
            for id in range(rng[0], rng[1]+1):
                id_str = str(id)
                try:
                    arr = split_into_chunks(id_str, 2)
                    if all_equal(arr):
                        count += id
                except ValueError:
                    pass
        return count

    # @answer(1234)
    def part_2(self) -> int:
        count = 0
        for rng in self.input:
            for id in range(rng[0], rng[1]+1):
                id_str = str(id)
                for chunks in range(2, len(id_str)+1):
                    try:
                        arr = split_into_chunks(id_str, chunks)
                        if all_equal(arr):
                            count += id
                            break
                    except ValueError:
                        pass

        return count

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
