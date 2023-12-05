from test import star_one_two, star_one_ex
from collections import defaultdict


class Solution:
    # Star 1
    """
    Notes:
        (destination, source, range - 1)

        source = x
        map ~ (d, s, r)

        if x belongs to [s, s + r - 1]
        then x maps to d + (s - x)
        else try different map

        if no map then x maps to x
    """

    def parse_input(self, input):
        maps = []
        lines = input.splitlines()
        seeds = lines[0].split(":")[1].strip().split()
        # print(seeds)
        skip = False
        for index, line in enumerate(lines[1:]):
            if not line:
                maps.append([])
                skip = True
                continue
            if skip:
                skip = False
                continue

            [d, s, r] = map(lambda x: int(x), line.split())
            # maps store arrays that store mappings
            # a mapping has, (range, low_bound_source, high_bound_source, dest)
            maps[-1].append((r, s, s + r - 1, d))

        return (seeds, maps)

    def star_one(self, input: str):
        res = float("inf")
        (seeds, maps) = self.parse_input(input)
        for seed in seeds:
            source = int(seed)
            dest = source
            for _map in maps:
                for mapping in _map:
                    if mapping[1] <= source <= mapping[2]:
                        dest = mapping[3] + (source - mapping[1])
                        break
                source = dest
                dest = source

            res = min(dest, res)

        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:
        rip the brute force (reached 31gb ram in 30secs of running the part 1 algo lol)
        bucket based approach break seed ranges into sub ranges based on mappings
    """

    def star_two(self, input):
        res = float("inf")

        (seeds, maps) = self.parse_input(input)
        all_seeds = []
        for i in range(0, len(seeds), 2):
            val = int(seeds[i])
            for x in range(int(seeds[i + 1])):
                all_seeds.append(val + x)

        for seed in all_seeds:
            source = int(seed)
            dest = source
            for _map in maps:
                for mapping in _map:
                    if mapping[1] <= source <= mapping[2]:
                        dest = mapping[3] + (source - mapping[1])
                        break
                source = dest
                dest = source

            res = min(dest, res)
        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()
    solution.star_one(star_one_ex)
    solution.star_two(star_one_ex)

    print("\n\nMain Solution:")
    sol_one = solution.star_one(star_one_two)
    # sol_two = solution.star_two(star_one_two)
    print("Done!")


if __name__ == "__main__":
    main()
