from test import star_one, star_two, example, example2, example3


class Solution:
    # Star 1
    """
    Notes:
    """

    def parse_input(self, input):
        [instructions, maps] = input.split("\n\n")
        mappings = {}
        starts = []
        for dir in maps.splitlines():
            [key, val] = dir.split("=")
            (left, right) = val.split(", ")
            key = key.strip()
            mappings[key] = (left[2:], right[:-1])
            if key[-1] == "A":
                starts.append(key)

        return instructions, mappings, starts

    map_dir = {"L": 0, "R": 1}

    def star_one(self, input: str):
        if not input:
            return
        res = 0
        instructions, mappings, _ = self.parse_input(input)

        pos = 0
        curr = "AAA"
        end = "ZZZ"
        while True:
            curr = mappings[curr][self.map_dir[instructions[pos]]]
            res += 1

            if curr == end:
                break
            pos = (pos + 1) % len(instructions)

        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:

    """

    def star_two(self, input):
        if not input:
            return
        res = 0
        instructions, mappings, starts = self.parse_input(input)

        pos = 0
        print(starts)
        while not all(map(lambda x: x[-1] == "Z", starts)):
            res += 1
            for index, curr in enumerate(starts):
                starts[index] = mappings[curr][self.map_dir[instructions[pos]]]
            pos = (pos + 1) % len(instructions)
            print(res, starts)
        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()
    solution.star_one(example)
    solution.star_one(example2)
    solution.star_two(example3)

    print("\n\nMain Solution:")
    sol_one = solution.star_one(star_one)
    sol_two = solution.star_two(star_two)
    print("Done!")


if __name__ == "__main__":
    main()
