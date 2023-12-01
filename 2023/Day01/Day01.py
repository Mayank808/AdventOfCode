from test import star_one, star_two


class Solution:
    # Star 1
    """
    Notes:
        Simple for loop to find first and last numbers in lines
        - Could have used an array but not needed
    """

    def star_one(self, input: str):
        res = 0
        for line in input.splitlines():
            first, last = "", ""
            for char in line:
                if not char.isdigit():
                    continue
                if not first:
                    first = char
                last = char

            num = first + last
            if not num:
                continue
            res += int(num)
            # print(f"Processed: {line}, found {num} and total is {res}.")

        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:
        Created a mapping dictionary to find strings in input cleanly.
        Brute force method by using starts with built in function. 
        Ideal solution would probably use a prebuilt digit trie to parse the input and return valid state digits.
    """

    num_word = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    def star_two(self, input):
        res = 0
        for line in input.splitlines():
            first, last = "", ""
            for i, char in enumerate(line):
                if char.isdigit():
                    if not first:
                        first = char
                    last = char

                for key, val in self.num_word.items():
                    if line[i:].startswith(key):
                        if not first:
                            first = val
                        last = val
                        break

            num = first + last
            if not num:
                continue
            res += int(num)
            # print(f"Processed: {line}, found {num} and total is {res}.")

        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()

    solution.star_one(
        """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    )
    solution.star_one("fewfw31321efewf")
    solution.star_one("fewfwefewf")

    solution.star_two(
        """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    )

    print("\n\nMain Solution:")
    solution.star_one(star_one)
    solution.star_two(star_two)
    print("Done!")


if __name__ == "__main__":
    main()
