from test import star_one, star_two, example


class Solution:
    # Star 1
    """
    Notes:
    Rows = reports Columnns = Levels
    levels always increasing or decreasing
    and two levels have a difference between 1 and 3
    """

    def parse_input(self, input):
        print(f"Use if required {input}")

    def star_one(self, input: str):
        if not input:
            return
        res = 0
        
        for report in input.splitlines():
            if not report:
                continue
            
            levels = report.split()
            
            prev_diff = 0
            for i in range(1, len(levels)):
                diff = int(levels[i]) - int(levels[i-1])
                if abs(diff) < 1 or abs(diff) > 3:
                    break
                
                if prev_diff and prev_diff * diff < 0:
                    break
                
                prev_diff = diff
            else:
                res += 1

        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:
    Can now remove one level from the report
    Check all possible removal combinations to see if there is a valid state for each report
    """
    
    def invalid_report_state(self, diff, prev_diff):
        return abs(diff) < 1 or abs(diff) > 3 or (prev_diff and prev_diff * diff < 0)

    def star_two(self, input):
        if not input:
            return
        res = 0
        
        for report in input.splitlines():
            if not report:
                continue
            
            levels = list(map(int, report.split()))
            
            valid = False
            for skip in range(len(levels)):
                level = levels[:skip] + levels[skip + 1:]
                
                prev_diff = 0    
                for i in range(1, len(level)):
                    diff = level[i] - level[i-1]
                    if abs(diff) < 1 or abs(diff) > 3:
                        break
                
                    if prev_diff and prev_diff * diff < 0:
                        break
                
                    prev_diff = diff
                else:
                    valid = True
                    res += 1
                
                if valid:
                    break

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
