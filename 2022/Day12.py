from test import test

# Star 1
"""
Notes:
    Start at point S
    End at point E
    Use some sort of search algo to find shortest path
    simplistic A* style search algo:
        Heuristic Func: Min Manhatten Distance
        Cumulative Func: Steps taken to cur pos
        Minimize: Manhatten Distance + Steps To Date
    Also going to try to create a solution using and learning Djikstras Algo
        Need a refresher after implemnting this in cs136
"""
res = 0
print("Star 1: ", res)

# start search queue with start pos
# create a visited bool array defaulted to false
# Repeat:
    # Choose position from search queue with smallest steps to date and manhatten distance
    # For new pos check if it is End pos if it is return
    # Since it is not end pos find all squares top, bottom, left, right that are not true in 
    #   visited or search queue and add them to the search queue with step incremented
# repeat above until a solution is achieved


# Star 2
"""
Notes:

"""
res = 0


print("Star 2: ", res)

