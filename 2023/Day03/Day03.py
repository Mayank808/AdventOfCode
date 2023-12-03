from test import star_one, star_two
from collections import defaultdict


class Solution:
    # Star 1
    """
    Notes:
        Initial Assumptions:
            Numbers are considered to only exist in rows (same line)
            No negative numbers
            Numbers are not considered symbols

        Initial Errors/Forgotten Edge cases:
            Was getting an answer slightly below the actual answer because
            I forgot to account for numbers at the end of a line. Added
            condition before continue to account for this

        Takeaway:
            Think of all possible edge cases carefully and insure initialy assumptions are correct.
            Overall had a correct bruteforce apporach just forgot to handle one edge case properly.
    """

    def is_symbol(self, char):
        return not char == "." and not char.isdigit()

    def star_one(self, input: str):
        res = 0

        matrix = [[char for char in line] for line in input.splitlines()]
        symbols = set()

        for row, line in enumerate(matrix):
            for col, char in enumerate(line):
                if self.is_symbol(char):
                    symbols.add((row, col))

        for row, line in enumerate(matrix):
            num = ""
            for col, char in enumerate(line):
                if char.isdigit():
                    num += char
                    if col != len(matrix[0]) - 1:
                        continue

                if num:
                    x, y = row - 1, col - len(num) - 1
                    valid = False
                    for row_check in range(3):
                        for col_check in range(len(num) + 2):
                            check_x, check_y = x + row_check, y + col_check
                            if (check_x, check_y) in symbols:
                                valid = True

                    if valid:
                        res += int(num)
                num = ""

        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:
        Second problem was significanlty more straightforward once first was cleared.
        Main blocker on first was the edge case i didnt account for with numbers at the end of lines.
        
        Simply added a dictionary to store adjecent numbers to stars found in array.
        If arrays in dict have 2 numbers we have a valid gear hence multiply and add.
    """

    def star_two(self, input):
        res = 0

        matrix = [[char for char in line] for line in input.splitlines()]
        symbols = set()

        for row, line in enumerate(matrix):
            for col, char in enumerate(line):
                if self.is_symbol(char):
                    symbols.add((row, col))

        gears = defaultdict(list)
        for row, line in enumerate(matrix):
            num = ""
            for col, char in enumerate(line):
                if char.isdigit():
                    num += char
                    if col != len(matrix[0]) - 1:
                        continue

                if num:
                    x, y = row - 1, col - len(num) - 1
                    valid = False
                    for row_check in range(3):
                        for col_check in range(len(num) + 2):
                            check_x, check_y = x + row_check, y + col_check
                            if (check_x, check_y) in symbols:
                                if matrix[check_x][check_y] == "*":
                                    gears[(check_x, check_y)].append(num)

                num = ""

        for value in gears.values():
            if len(value) == 2:
                res += int(value[0]) * int(value[1])
        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()
    solution.star_one(
        """467......*
...*...114"""
    )
    solution.star_two(
        """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    )

    print("\n\nMain Solution:")
    sol_one = solution.star_one(star_one)
    sol_two = solution.star_two(star_two)
    print("Done!")


if __name__ == "__main__":
    main()
