from test import star_one_two, star_one_ex


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
        seeds = list(map(int, lines[0].split(":")[1].strip().split()))
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

            [d, s, r] = map(int, line.split())
            # maps store arrays that store mappings
            # a mapping has, (range, low_bound_source, high_bound_source, dest)
            maps[-1].append((r, s, s + r - 1, d))

        return (seeds, maps)

    def star_one(self, input: str):
        res = float("inf")
        (seeds, maps) = self.parse_input(input)
        # print(seeds)
        for seed in seeds:
            source = seed
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
        bucket based approach break seed ranges into sub ranges based on mapping intersections.
        compute intersection between two ranges
    """

    def star_two(self, input):
        res = 0

        (input_seeds, maps) = self.parse_input(input)

        # brute force if this worked it would have been great
        # all_seeds = []
        # for i in range(0, len(seeds), 2):
        #     val = int(seeds[i])
        #     for x in range(int(seeds[i + 1])):
        #         all_seeds.append(val + x)
        seeds = []
        # print(input_seeds)
        for i in range(0, len(input_seeds), 2):
            seeds.append((input_seeds[i], input_seeds[i] + input_seeds[i + 1] - 1))

        for _map in maps:
            mapped_seeds = []
            while seeds:
                seed = seeds.pop()

                for mapping in _map:
                    # compute interval
                    r, low, up, dest = mapping
                    start = max(seed[0], low)
                    end = min(seed[1], up)
                    # print("iter")
                    # print("seed", seed)
                    # print("mapping", mapping)
                    # print("interval", (start, end))

                    # proper interval
                    if start < end:
                        # print("valid")
                        # append mapped interval
                        mapped_seeds.append((dest + start - low, dest + end - low))

                        # compute subranges of unmapped portion of interval
                        if start > seed[0]:
                            seeds.append((seed[0], low - 1))

                        if end < seed[1]:
                            seeds.append((end + 1, seed[1]))
                        break
                else:
                    mapped_seeds.append(seed)
            seeds = mapped_seeds
        res = min(seeds)[0]
        # for seed in seeds:
        #     res = min(0, res)
        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()
    solution.star_one(star_one_ex)
    solution.star_two(star_one_ex)

    print("\n\nMain Solution:")
    sol_one = solution.star_one(star_one_two)
    sol_two = solution.star_two(star_one_two)
    print("Done!")


if __name__ == "__main__":
    main()
