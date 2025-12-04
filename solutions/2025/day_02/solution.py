# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import IntSplit2RowSolution, answer
import re


class Solution(IntSplit2RowSolution):
    _year = 2025
    _day = 2

    separator = ","
    separator2 = "-"

    def solve(self) -> tuple[int, int]:
        count1 = 0
        count2 = 0
        for rng in self.input:
            for id in range(rng[0], rng[1] + 1):
                self.spinner()
                id_str = str(id)
                if re.search(r"^(\d+)\1$", id_str):
                    count1 += id
                if re.search(r"^(\d+)\1+$", id_str):
                    count2 += id
        return (count1, count2)
