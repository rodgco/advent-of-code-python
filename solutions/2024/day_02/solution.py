# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import AnyFunSolution
from functools import reduce


class Solution(AnyFunSolution):
    _year = 2024
    _day = 2

    def fun(self, line):
        return list(map(int, line.split(" ")))




    # @answer(1234)
    def part_1(self) -> int:
        for report in self.input:
            # Defining function here to enclosure `report`
            def build_report_safety_data(acc, item):
                index, value = item
                print(f"Acc: {acc}, Index: {index}, Value: {value}")
                if index < len(report)-1:
                    acc.append(value - report[index+1])
                return acc

            safety = reduce(build_report_safety_data, enumerate(report), [])
            
            evaluate_safety(safety)

        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
