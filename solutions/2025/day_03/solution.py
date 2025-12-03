# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from ...base import AnyFunSolution


class Solution(AnyFunSolution):
    _year = 2025
    _day = 3

    def fun(self, line):
        return [int(digit) for digit in line]

    # @answer(1234)

    def part_1(self) -> int:
        total_joltage = 0
        for bank in self.input:
            max_joltage = 0
            batteries_count = len(bank)
            for index, first_rating in enumerate(bank):
                for second_rating in bank[index + 1 :]:
                    joltage = first_rating * 10 + second_rating
                    max_joltage = max(joltage, max_joltage)

            total_joltage += max_joltage

        return total_joltage

    # @answer(1234)

    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
