# Generated using @rodgco's AoC Python Template: https://github.com/rodgco/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

import re

from ...base import IntSplit2RowSolution


class Solution(IntSplit2RowSolution):
    _year = 2025
    _day = 2

    separator = ","
    separator2 = "-"

    def solve(self) -> tuple[int, int]:
        count1 = 0
        count2 = 0
        for rng in self.input:
            for product_id in range(rng[0], rng[1] + 1):
                self.spinner()
                id_str = str(product_id)
                if re.search(r"^(\d+)\1$", id_str):
                    count1 += product_id
                if re.search(r"^(\d+)\1+$", id_str):
                    count2 += product_id
        return (count1, count2)
