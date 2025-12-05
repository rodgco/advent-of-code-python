# Generated using @rodgco's AoC Python Template: https://github.com/rodgco/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from ...base import AnyFullFunSolution


def overlap(rng1, rng2):
    start1, stop1 = rng1
    start2, stop2 = rng2

    range1 = range(start1, stop1)
    range2 = range(start2, stop2)

    return (
        start1 in range2
        or stop1 in range2
        or start2 in range1
        or stop2 in range1
        or start2 == stop1 + 1
        or stop1 == start2
    )


def merge_ranges(rng1, rng2):
    start1, stop1 = rng1
    start2, stop2 = rng2

    return (min(start1, start2), max(stop1, stop2))


class Solution(AnyFullFunSolution):
    _year = 2025
    _day = 5

    def fun(self, data):
        ranges_block, ids_block = data.split("\n\n")

        ranges = [
            (item[0], item[1])
            for item in [
                tuple(map(int, rng.split("-"))) for rng in ranges_block.split("\n")
            ]
        ]
        ids = [int(ingredient) for ingredient in ids_block.split("\n")]

        return (ranges, ids)

    def part_1(self) -> int:
        ranges, ids = self.input

        fresh = 0

        for ingredient in ids:
            for start, stop in ranges:
                if ingredient in range(start, stop + 1):
                    fresh += 1
                    break

        return fresh

    def part_2(self) -> int:
        ranges, ids = self.input

        sorted_ranges = sorted(ranges, key=lambda rng: rng[0])

        for idx1, rng1 in enumerate(sorted_ranges[:-1]):
            if rng1 is None:
                continue
            for idx2, rng2 in enumerate(sorted_ranges[idx1 + 1 :]):
                if rng2 is None:
                    continue
                if overlap(rng1, rng2):
                    rng1 = merge_ranges(rng1, rng2)
                    sorted_ranges[idx1] = rng1
                    sorted_ranges[idx1 + idx2 + 1] = None

        count = 0
        for rng in sorted_ranges:
            if rng is None:
                continue
            count += rng[1] - rng[0] + 1

        return count
