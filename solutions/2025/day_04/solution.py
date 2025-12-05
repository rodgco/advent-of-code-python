# Generated using @rodgco's AoC Python Template: https://github.com/rodgco/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4

from ...base import AnyFullFunSolution


def map_adjacents(location_of_paper_rolls):
    adjacent_map = {}

    adjacent_deltas = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for row, col in location_of_paper_rolls:
        adjacent_map.setdefault((row, col), 0)
        for deltas in adjacent_deltas:
            r = row + deltas[0]
            c = col + deltas[1]
            if (r, c) in location_of_paper_rolls:
                adjacent_map.setdefault((r, c), 0)
                adjacent_map[(r, c)] += 1

    return adjacent_map


def remove_roll_from_map(adjacent_map, location):
    row, col = location
    adjacent_map.pop(location)
    for row_delta in range(-1, 2):
        for col_delta in range(-1, 2):
            r = row + row_delta
            c = col + col_delta
            if (r, c) in adjacent_map and (row_delta, col_delta) != (0, 0):
                adjacent_map[(r, c)] -= 1


class Solution(AnyFullFunSolution):
    _year = 2025
    _day = 4

    def fun(self, data):
        location_of_paper_rolls = []

        for row, line in enumerate(data.split("\n")):
            for col, value in enumerate(line):
                if value == "@":
                    location_of_paper_rolls.append((row, col))

        self.debug(f"Starting with {len(location_of_paper_rolls)} rolls.")

        return map_adjacents(location_of_paper_rolls)

    def part_1(self) -> int:
        count = 0

        adjacent_map = self.input

        for value in adjacent_map.values():
            if value < 4:
                count += 1

        return count

    def part_2(self) -> int:
        count = 0

        while True:
            round_count = 0
            locations = list(self.input.keys())
            for location in locations:
                value = self.input.get(location)
                if value < 4:
                    round_count += 1
                    remove_roll_from_map(self.input, location)

            if round_count == 0:
                break

            count += round_count

        return count
