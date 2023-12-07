from test import stars, example


class Solution:
    # Star 1
    """
    Notes:
        t = total_time
        d = beat_distance
        h = held button for time

        want to maximize distance traveled by optamizing this function
        distance traveled (x) = h * (t - h) where h <= t
        note above is a QUADRATIC functon.

        want to find lower bound and upperbound on h to allow distance traveled to be > d
        can use binary search to find lower and upper bound on time such that that distance traveled > d

        could also brute force the quadratic but binary search is optimal solution
        
        other solutions 
        - quadratic formula (have to still compute sqrt)
        - brute force the quadratic 
    """

    def star_one(self, input: str):
        res = 1
        [times, distances] = input.splitlines()
        times = list(map(int, times.split(":")[1].strip().split()))
        distances = list(map(int, distances.split(":")[1].strip().split()))

        for time, distance in zip(times, distances):
            left, right = 0, time

            # finding min
            while left < right:
                mid_time_held = (left + right) // 2
                distance_travelled = (time - mid_time_held) * mid_time_held

                if distance_travelled > distance:
                    right = mid_time_held
                else:
                    left = mid_time_held + 1

            min_time = left

            # not needed relize that a quadratic is symmetric as such max_time = t - min_time
            # find max

            # left, right = 0, time
            # while left < right:
            #     mid_time_held = (left + right) // 2
            #     distance_travelled = (time - mid_time_held) * mid_time_held
            #     if distance_travelled >= distance:
            #         left = mid_time_held + 1
            #     else:
            #         right = mid_time_held
            # max_time = left

            max_time = time - min_time + 1
            res *= max_time - min_time
            # print("min max:", min_time, max_time)
            # print(res)

        # print(times, distances)
        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:
        Since star 1 was done with an optimal solution.
        Star two was simply changing how input was handled. 
        This is probably still possible with brute force unlike day 5
    """

    def star_two(self, input):
        res = 0
        [times, distances] = input.splitlines()

        # only difference between one and two is how we handle input
        time = int("".join(times.split(":")[1].split()))
        distance = int("".join(distances.split(":")[1].split()))
        # print(time, distance)

        left, right = 0, time
        # finding min
        while left < right:
            mid_time_held = (left + right) // 2
            distance_travelled = (time - mid_time_held) * mid_time_held

            if distance_travelled > distance:
                right = mid_time_held
            else:
                left = mid_time_held + 1

        min_time = left
        max_time = time - min_time + 1

        res = max_time - min_time

        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()
    solution.star_one(example)
    solution.star_two(example)

    print("\n\nMain Solution:")
    sol_one = solution.star_one(stars)
    sol_two = solution.star_two(stars)
    print("Done!")


if __name__ == "__main__":
    main()
