# Generated using @rodgco's AoC Python Template: https://github.com/rodgco/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6


import re
from functools import reduce
from operator import add, mul

from ...base import TextSolution


class Solution(TextSolution):
    _year = 2025
    _day = 6

    def part_1(self) -> int:
        pattern = r"\s+"

        lines = self.input.split("\n")
        numbers = list(
            zip(*(map(int, re.split(pattern, line.strip())) for line in lines[:-1]))
        )
        symbols = re.split(pattern, lines[-1].strip())

        switch = {"+": (add, 0), "*": (mul, 1)}
        count = 0

        for index, operation in enumerate(symbols):
            op = switch.get(operation)
            result = reduce(op[0], numbers[index], op[1])
            count += result

        return count

    def part_2(self) -> int:
        lines = self.input.split("\n")

        numbers_blocks = lines[:-1]
        symbols_line = lines[-1]

        self.debug(numbers_blocks, symbols_line)

        count = 0
        numbers = []

        for index in range(len(symbols_line) - 1, -1, -1):
            number_string = ""
            for line in numbers_blocks:
                number_string += line[index]

            self.debug(f"{index} => {number_string}")

            if number_string.strip() != "":
                numbers.append(int(number_string))

            if symbols_line[index] == "+":
                value = reduce(add, numbers, 0)
                self.debug(f"Adding: {numbers} -> {value}")
                count += value
                numbers = []
            elif symbols_line[index] == "*":
                value = reduce(mul, numbers, 1)
                self.debug(f"Mult: {numbers} -> {value}")
                count += value
                numbers = []

        return count
