# Generated using @rodgco's AoC Python Template: https://github.com/rodgco/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/7

from functools import reduce
from operator import add

from ...base import AnyFullFunSolution


class Solution(AnyFullFunSolution):
    _year = 2025
    _day = 7

    def fun(self, data):
        lines = data.split("\n")

        start = None
        splitters = []
        depth = len(lines)

        for row, line in enumerate(lines):
            for col, value in enumerate(line):
                if value == "S":
                    start = (row, col)
                elif value == "^":
                    splitters.append((row, col))

        return start, splitters, depth

    def part_1(self) -> int:
        start, splitters, depth = self.input

        beams = {start}
        count = 0

        for index in range(1, depth):
            new_beams = set()
            for beam in beams:
                if (beam[0] + 1, beam[1]) in splitters:
                    beam_left = (beam[0] + 1, beam[1] - 1)
                    beam_right = (beam[0] + 1, beam[1] + 1)
                    new_beams |= {beam_left, beam_right}
                    count += 1
                else:
                    new_beams |= {(beam[0] + 1, beam[1])}
            beams = new_beams

        return count

    def part_2_brute_force(self) -> int:
        start, splitters, depth = self.input

        cache = {}

        def beamer(beam):
            count = 0
            if beam[0] == depth:
                self.debug(f"{beam}")
                return 1

            if beam in cache:
                self.debug(f"Hit cache {beam} {cache[beam]}")
                return cache[beam]

            if (beam[0] + 1, beam[1]) in splitters:
                count += beamer((beam[0] + 1, beam[1] - 1))
                count += beamer((beam[0] + 1, beam[1] + 1))
            else:
                count += beamer((beam[0] + 1, beam[1]))

            cache[beam] = count
            return count

        return beamer(start)

    def part_2(self) -> int:
        start, splitters, depth = self.input

        beams = {start[1]: 1}

        for index in range(1, depth):
            new_beams = beams.copy()
            for beam, current in beams.items():
                if (index, beam) in splitters:
                    new_beams[beam - 1] = new_beams.setdefault(beam - 1, 0) + current
                    new_beams[beam + 1] = new_beams.setdefault(beam + 1, 0) + current
                    new_beams.pop(beam)
            beams = new_beams

        return reduce(add, beams.values(), 0)
