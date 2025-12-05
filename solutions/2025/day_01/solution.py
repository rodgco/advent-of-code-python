# Generated using @rodgco's AoC Python Template: https://github.com/rodgco/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrMatchRegexpSolution


class Solution(StrMatchRegexpSolution):
    _year = 2025
    _day = 1
    regexp = r"(L|R)(\d+)"

    def solve(self) -> tuple[int, int]:
        dial = 50
        count1 = 0
        count2 = 0

        for rotation in self.input:
            direction = rotation[0]
            clicks = int(rotation[1])

            dial_ant = dial

            count2 += clicks // 100
            dial += (1 if direction == "R" else -1) * (clicks % 100)

            if dial in {0, 100}:
                dial = 0
                count1 += 1
                count2 += 1
            elif dial < 0:
                dial += 100
                if dial_ant != 0:
                    count2 += 1
            elif dial > 99:
                dial -= 100
                if dial_ant != 0:
                    count2 += 1

        return (count1, count2)
