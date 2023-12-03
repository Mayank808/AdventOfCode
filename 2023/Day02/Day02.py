from test import star_one, star_two


class Solution:
    # Star 1
    """
    Notes:
        Straightforward problem.
        Parse input properly into clean subarrays that repersent each grab.
        Loop through the grab to check if the blocks found are below max number of blocks allowed.
        Main issue was just ensuring the input was parsed properly.
    """

    def parse_input(self, line):
        [game, hands] = line.split(":")
        game = int(game.removeprefix("Game "))
        hands = hands.split(";")
        grabs = [
            list(map(lambda x: x.strip().split(" "), hand.split(","))) for hand in hands
        ]
        return (game, grabs)

    max_blocks = {"red": 12, "green": 13, "blue": 14}

    def star_one(self, input: str):
        res = 0
        for line in input.splitlines():
            (game, grabs) = self.parse_input(line)

            valid = True
            for grab in grabs:
                for block in grab:
                    if self.max_blocks[block[1]] < int(block[0]):
                        valid = False
                        break

            if valid:
                res += game

            # print(f"Game {game}: plays {grabs}")

        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:
        Builds on last problem except in this one we need to ensure all games are valid,
        by finding the minimum number of blocks needed to validate the game.
        Simply loop through blocks grab and find max number of each colour.
        Compute power on the resulting array. 
    """

    def power(self, min_values: dict[str, int]):
        res = 1

        for _, val in min_values.items():
            res *= val
        return res

    def star_two(self, input):
        res = 0

        for line in input.splitlines():
            (game, grabs) = self.parse_input(line)
            min_possible = {}
            for grab in grabs:
                for block in grab:
                    if (
                        not block[1] in min_possible
                    ):  # cleaner way to not have to init all colour values to float('inf')
                        min_possible[block[1]] = int(block[0])
                        continue
                    min_possible[block[1]] = max(int(block[0]), min_possible[block[1]])

            # print(min_possible)
            res += self.power(min_possible)

        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()
    solution.star_one("")
    solution.star_two("")

    print("\n\nMain Solution:")
    sol_one = solution.star_one(star_one)
    sol_two = solution.star_two(star_two)
    print("Done!")


if __name__ == "__main__":
    main()
