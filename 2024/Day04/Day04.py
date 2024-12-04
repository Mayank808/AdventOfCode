from test import star_one, star_two, example, example2


class Solution:
    # Star 1
    """
    Notes:
    """

    def parse_input(self, input):
        print(f"Use if required {input}")
        
    def check_paths(self, grid, row, col, find):
        res = 0
        
        for (r, c) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            
            for i in range(0, len(find)):
                if not(0 <= row + r * i < len(grid)) or not(0 <= col + c * i < len(grid[0])) or grid[row + r * i][col + c * i] != find[i]:
                    break
            else:
                res += 1
            
        
        return res

    def star_one(self, input: str):
        if not input:
            return
        res = 0

        find = "XMAS"
        grid = [list(line) for line in input.splitlines()]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == find[0]:
                    res += self.check_paths(grid, row, col, find)
                        
        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:
    Look for A check corners.
    
    Code Simplifications:
    1. Reduce if conditions by not checking edges. 
    2. Instead of what Find_x does get corners in order and compare directly with 4 possible valid permutations.
       - MMSS, SSMM, MSMS, SMMS are the only valid permutations for the corners.
    """
    def find_x(self, grid, row, col):
        for r, c in [(-1, -1), (-1, 1)]:
            l1 = grid[row + r][col + c]
            l2 = grid[row + r * -1][col + c * -1]
            
            if not(l1 == "M" and l2 == "S" or l1 == "S" and l2 == "M"):
                return 0
        
        return 1
        
    def star_two(self, input):
        if not input:
            return
        res = 0
        
        grid = [list(line) for line in input.splitlines()]
        
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                if grid[row][col] == "A":
                    res += self.find_x(grid, row, col)

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
