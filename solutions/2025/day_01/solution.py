# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrMatchRegexpSolution, answer
import re


class Solution(StrMatchRegexpSolution):
    _year = 2025
    _day = 1
    regexp = r'(L|R)(\d+)'

    # @answer(1234)
    # def part_1(self) -> int:
    #     dial = 50
    #     count = 0
    #
    #     for rotation in self.input:
    #         direction = rotation[0]
    #         clicks = int(rotation[1])
    #
    #         dial += (1 if direction == "R" else -1) * (clicks % 100)
    #
    #         if dial > 99:
    #             dial -= 100
    #         elif dial < 0:
    #             dial += 100
    #
    #         if dial == 0:
    #             count += 1
    #
    #     return count

    # @answer(1234)
    # def part_2(self) -> int:
    #     dial = 50
    #     count = 0
    #
    #     for rotation in self.input:
    #         direction = rotation[0]
    #         clicks = int(rotation[1])
    #
    #         dial += (1 if direction == "R" else -1) * clicks
    #
    #         while dial < 0 and dial > 99:
    #             if dial < 0:
    #                 dial += 100
    #                 count += 1
    #             elif dial == 100:
    #                 dial = 0
    #             elif dial > 99:
    #                 dial -= 100
    #                 count += 1
    #
    #         if dial == 0:
    #             count += 1
    #
    #     return count

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        dial = 50
        count1 = 0
        count2 = 0

        for rotation in self.input:
            direction = rotation[0]
            clicks = int(rotation[1])

            self.debug(f"1 ==> Dir: {direction}, Clk: {clicks}, Dial: {
                       dial}, C1: {count1}, C2: {count2}")

            dial_ant = dial

            count2 += clicks // 100
            dial += (1 if direction == "R" else -1) * (clicks % 100)

            if dial == 0 or dial == 100:
                self.debug("Dial at 0")
                dial = 0
                count1 += 1
                count2 += 1
            elif dial < 0:
                self.debug("Dial crossed 0")
                dial += 100
                if dial_ant != 0:
                    count2 += 1
            elif dial > 99:
                self.debug("Dial crossed 0")
                dial -= 100
                if dial_ant != 0:
                    count2 += 1

            self.debug(f"2 ==> Dial: {dial}, C1: {count1}, C2: {count2}")
            self.debug("------------------")

        return (count1, count2)
