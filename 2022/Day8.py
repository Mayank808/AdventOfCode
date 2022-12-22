from test import test
from enum import Enum
# Star 1
"""
Notes:
    BFS and DP from each position going up down left and right
    At each position make a decision
"""
res = 0
trees = []
for line in test.splitlines():
    trees.append([int(x) for x in line])
visible_trees = [[False] * len(trees[0]) for x in trees]
rows = len(trees)
cols = len(trees[0])
 
for row in range(rows):
    max_height = -1
    for col in range(cols):
        cur_height = trees[row][col]
        if not visible_trees[row][col] and cur_height > max_height:
            res += 1
            visible_trees[row][col] = True
        max_height = max(max_height, cur_height)
    max_height = -1
    for col in range(cols - 1, -1, -1):
        cur_height = trees[row][col]
        if not visible_trees[row][col] and cur_height > max_height:
            res += 1
            visible_trees[row][col] = True
        max_height = max(max_height, cur_height) 
        
for col in range(cols):
    max_height = -1
    for row in range(rows):
        cur_height = trees[row][col]
        if not visible_trees[row][col] and cur_height > max_height:
            res += 1
            visible_trees[row][col] = True
        max_height = max(max_height, cur_height)
    max_height = -1
    for row in range(rows - 1, -1, -1):
        cur_height = trees[row][col]
        if not visible_trees[row][col] and cur_height > max_height:
            res += 1
            visible_trees[row][col] = True
        max_height = max(max_height, cur_height)    

print("Star 1: ", res)

# Star 2
"""
Notes:

"""
res = -1
for row in range(rows):
    for col in range(cols):
        left = [trees[x][col] for x in range(row - 1, -1, -1)]
        right = [trees[x][col] for x in range(row + 1, rows)]
        up = [trees[row][x] for x in range(col - 1, -1, -1)]
        down = [trees[row][x] for x in range(col + 1, cols)]
        
        total_score = 1
        for check in (left, right, up, down):
            curr_score = 0
            for x in check:
                curr_score += 1
                if x >= trees[row][col]:
                    break
            total_score *= curr_score
        res = max(res, total_score)


print("Star 2: ", res)

