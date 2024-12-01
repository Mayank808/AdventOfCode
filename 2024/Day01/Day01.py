from test import star_one, star_two, example
import heapq

class Solution:
    # Star 1
    """
    Notes:
    """

    def parse_input(self, input):
        print(f"Use if required {input}")

    def star_one(self, input: str):
        if not input:
            return
        res = 0
        
        lines = input.splitlines()
        left, right = [], []
        
        for line in lines:
            l, r = map(int, line.split())
            heapq.heappush(left, l)
            heapq.heappush(right, r)
        
        
        while left:
            l = heapq.heappop(left)
            r = heapq.heappop(right)
            res += abs(r - l)
        
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
        
        lines = input.splitlines()
        left, right = [], {}
        
        for line in lines:
            l, r = map(int, line.split())
            
            left.append(l)
            right[r] = right.get(r, 0) + 1
        
        for key in left:
            count = right.get(key, 0)
            res += count * key


        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()
    solution.star_one(example)
    solution.star_two(example)

    print("\n\nMain Solution:")
    sol_one = solution.star_one(star_one)
    sol_two = solution.star_two(star_two)
    print("Done!")


if __name__ == "__main__":
    main()
