from test import star_one, star_two


class Solution:
    # Star 1
    """
    Notes:
    """

    def star_one(self, input: str):
        res = 0

        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:

    """

    def star_two(self, input):
        res = 0

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
