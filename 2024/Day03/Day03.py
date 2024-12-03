from test import star_one, star_two, example, example2
import re

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
    
        pattern = r"mul\(\d+,\d+\)"
        
        for match in re.finditer(pattern, input):
            left, right = map(int, match.group()[4:-1].split(","))
            
            res += left * right

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
        
        patterns = [r"mul\(\d+,\d+\)", r"don\'t\(\)", r"do\(\)"]
        events = []
        
        for index, pattern in enumerate(patterns):
            for match in re.finditer(pattern, input):
                events.append((match.start(), match.group()))
        
        events.sort(key=lambda x: x[0])
        
        skip = False
        for index, event in enumerate(events):
            start, match = event
            
            if match == "don't()":
                skip = True
            elif match == "do()":
                skip = False
            elif not skip:
                left, right = map(int, match[4:-1].split(","))
                res += left * right
                

        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()
    solution.star_one(example)
    solution.star_two(example2)

    print("\n\nMain Solution:")
    sol_one = solution.star_one(star_one)
    sol_two = solution.star_two(star_one)
    print("Done!")


if __name__ == "__main__":
    main()
