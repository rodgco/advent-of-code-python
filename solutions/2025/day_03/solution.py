#  Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from ...base import AnyFunSolution
from ...utils.arr_utils import join_to_string


def remove_battery(bank, digits):
    while len(bank) > digits:
        battery_to_remove = None
        for index, first_rating in enumerate(bank):
            if index == len(bank) - 1:
                break
            second_rating = bank[index + 1]
            if first_rating < second_rating:
                battery_to_remove = index
                break

        if battery_to_remove == None:
            battery_to_remove = len(bank) - 1

        del bank[battery_to_remove]
    return join_to_string(bank)


class Solution(AnyFunSolution):
    _year = 2025
    _day = 3

    def fun(self, line):
        return [int(digit) for digit in line]

    def solve(self) -> tuple[int, int]:
        total_joltage_part1 = 0
        total_joltage_part2 = 0
        for bank in self.input:
            # As remove_battery will trim the bank let's work on the
            # least destructive first (part_2) and then continue to
            # the most destructive (part2)
            total_joltage_part2 += remove_battery(bank, 12)
            total_joltage_part1 += remove_battery(bank, 2)
        return (total_joltage_part1, total_joltage_part2)
