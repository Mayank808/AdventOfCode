from test import star_one, star_two
from collections import defaultdict


class Solution:
    # Star 1
    """
    Notes:
    """

    def parse_input(self, input):
        card = input.split(":")[1]
        [winning, own] = card.split("|")
        winning = set(winning.split())

        return [winning, own]

    def star_one(self, input: str):
        res = 0
        for line in input.splitlines():
            [winning, own] = self.parse_input(line)
            match = -1
            for number in own.split():
                if number in winning:
                    match += 1
            
            # can also use set intersection to find comminality
            # match = len(set(winning) & set(own.split()))

            if match != -1:
                res += pow(2, match)
        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:
        Initial thoughts 
            queue/array based dp approach.
            append values onto array. value = number of winnings
            len array is number of copies i have of a given card. 
            sub 1 from each value after computing card wins.
            pop 0's from queue
            
        Above approach could work but ended up using a 
        simple dp approach with a dictionary to build up the total cards.
        This was an initial solution thought but didnt go with this as it will require alot of memory usage.
        Easier approach however.
    """

    def star_two(self, input):
        res = 0
        copys = defaultdict(int)
        for index, line in enumerate(input.splitlines()):
            copys[index] += 1
            [winning, own] = self.parse_input(line)
            match = 0

            for number in own.split():
                if number in winning:
                    match += 1

            # can also use set intersection to find comminality
            # match = len(set(winning) & set(own.split()))

            for add in range(match):
                copys[index + add + 1] += copys[index]

        res = sum(copys.values())
        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()
    solution.star_one(
        """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    )
    solution.star_two(
        """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    )

    print("\n\nMain Solution:")
    sol_one = solution.star_one(star_one)
    sol_two = solution.star_two(star_two)
    print("Done!")


if __name__ == "__main__":
    main()
