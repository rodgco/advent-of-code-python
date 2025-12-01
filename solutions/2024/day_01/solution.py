# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import IntSplit2Solution


class Solution(IntSplit2Solution):
    _year = 2024
    _day = 1
    separator2 = "   "

    # @answer(1234)
    def part_1(self) -> int:
        [list1, list2] = self.input

        list1.sort()
        list2.sort()

        return sum(abs(a - b) for a, b in zip(list1, list2))

    # @answer(1234)
    def part_2(self) -> int:
        [list1, list2] = self.input

        return sum(a * list2.count(a) for a in list1)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
