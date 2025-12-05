# Generated using @rodgco's AoC Python Template: https://github.com/rodgco/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4

from ...base import AnyFullFunSolution


class Solution(AnyFullFunSolution):
    _year = 2025
    _day = 4

    def fun(self, input):
        d = {}
        data = input.split("\n")
        total_rows = len(data)
        total_cols = len(data[0])

        def add_neighbours(row, col):
            for rowd in range(-1, 2):
                for cold in range(-1, 2):
                    r = row + rowd
                    c = col + cold
                    if d.get((r, c)) is not None and (rowd, cold) != (0, 0):
                        d[(r, c)] += 1

        for row, line in enumerate(data):
            for col, value in enumerate(line):
                if value == "@":
                    d.setdefault((row, col), 0)

        for row, line in enumerate(data):
            for col, value in enumerate(line):
                if value == "@":
                    add_neighbours(row, col)

        return d

    # @answer(1234)

    def part_1(self) -> int:
        count = 0

        for value in self.input.values():
            if value < 4:
                count += 1

        return count

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
