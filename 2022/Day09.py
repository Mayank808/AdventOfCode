from test import test

# Star 1
"""
Notes:

"""
res = 0
visited = set() # an set of tuples (row, col) of visited positions by tail
head = [0, 0]
tail = [0, 0]
visited.add((tail[0], tail[1]))
for line in test.splitlines():
    line = line.split(' ')
    line[1] = int(line[1])
    move = [0, 0]
    if line[0] == "R":
        move[0] = 1
    elif line[0] == "L":
        move[0] = -1
    elif line[0] == "U":
        move[1] = 1
    else:
        move[1] = -1
        
    for x in range(line[1]):
        head[0] += move[0]
        head[1] += move[1]
        
        # distance is greater then 2 we need to move tail
        if (abs(head[0] - tail[0]) >= 2):
            tail[0] += move[0]
            # move diag if needed
            tail[1] = head[1]
            visited.add((tail[0], tail[1])) 
        # distance is greater then 2 we need to move tail
        elif (abs(head[1] - tail[1]) >= 2):
            tail[1] += move[1]
            # move diag if needed
            tail[0] = head[0]
            visited.add((tail[0], tail[1])) 
print("Star 1: ", len(visited))
# Star 2
"""
Notes:

"""
res = 0
visited = set() # an set of tuples (row, col) of visited positions by tail
# treat 0 as head and 9 as tail
rope = [[0, 0] for _ in range(10)]
sign = lambda a: (a>0) - (a<0)
visited.add((0, 0)) # adding starting pos
for line in test.splitlines():
    line = line.split(' ')
    line[1] = int(line[1])
    move = [0, 0]
    if line[0] == "R":
        move[0] = 1
    elif line[0] == "L":
        move[0] = -1
    elif line[0] == "U":
        move[1] = 1
    else:
        move[1] = -1
        
    for x in range(line[1]):
        rope[0][0] += move[0]
        rope[0][1] += move[1]
        for y in range(9):              
            # distance is greater then 2 we need to move tail
            # cant use old method as each knot moves respectively based on the knot infront
            # using difference simulates the same thing as the last one 
            diffX = rope[y][0] - rope[y + 1][0]
            diffY = rope[y][1] - rope[y + 1][1]
            if abs(diffX) > 1 or abs(diffY) > 1:
                rope[y + 1][0] += sign(diffX)
                rope[y + 1][1] += sign(diffY)  
                visited.add((rope[9][0], rope[9][1]))
print("Star 2: ", len(visited))

