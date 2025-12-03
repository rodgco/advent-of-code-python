# CHANGELOG

## Unreleased

### Utility Modules

- **arr_utils.py**: Added `all_equal()` function to check if all elements in an array are equal
- **text_utils.py**: Added text manipulation utilities:
  - `split_into_chunks()`: Split text into a specified number of chunks
  - `split_into_chunks_bysize()`: Split text into chunks of a specific size

### Base Solution Enhancements

- Added `--spinner` CLI flag to display spinner animation during long operations (useful for 2025 Day 2)
- Added new solution input type: `AnyFunSolution` for custom parsing logic
- Added `IntSplit2RowSolution` and `IntSplit2ColSolution` for 2D array parsing (row and column based)
- Added `IntSplit2Solution` for generic list of lists integer parsing
- Implemented automatic submission behavior (controlled by test mode and `--no-submit` flag)

### Solutions Completed

- **2025 Day 1**: Completed both parts
- **2025 Day 2**: Completed both parts with spinner support
- **2024 Day 1**: Completed
- **2024 Day 2**: Work in progress

## Initial Setup

_released `2025-11-30`_

- Integrated with [aocd](https://github.com/wimglenn/advent-of-code-data) for automatic puzzle input retrieval and answer submission
- Set up base solution framework with multiple input parsing modes
- Created utility modules structure in `solutions/utils/`
- Configured test input support and debugging capabilities
