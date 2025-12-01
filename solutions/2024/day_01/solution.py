# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import IntSplit2ColSolution


class Solution(IntSplit2ColSolution):
    _year = 2024
    _day = 1
    separator2 = "   "

    # @answer(1234)
    # def part_1(self) -> int:
    #     list1, list2 = self.input
    #
    #     list1 = list(list1)
    #     list2 = list(list2)
    #
    #     list1.sort()
    #     list2.sort()
    #
    #     return sum(abs(a - b) for a, b in zip(list1, list2))

    # @answer(1234)
    # def part_2(self) -> int:
    #     list1, list2 = self.input
    #
    #     # list1 = list(list1)
    #     # list2 = list(list2)
    #
    #     return sum(a * list2.count(a) for a in list1)

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        list1, list2 = self.input

        list1 = list(list1)
        list2 = list(list2)

        list1.sort()
        list2.sort()

        result1 = sum(abs(a - b) for a, b in zip(list1, list2))
        result2 = sum(a * list2.count(a) for a in list1)

        return (result1, result2)
