from test import test
from test import commands
# Star 1
"""
Notes:
    Create an array of queues based on number of rows
    For each command pop x boxes out of queue A and push onto queue B
    Queue/Stacks fall FIFO and this will mimic the stack of boxes
    Issue best method to parse starting stack
        - Rewrite input to be easily digistable (Difficult to Replicate)
        - Loop through each line 
        - Each 3 block index in the array maps to 1 index in the queue array
"""
rows = []
first = True
for line in test.splitlines():
    if first:
        for x in range(len(line)//4 + 1):
            rows.append([])
        first = False
    left = 0
    index = 0
    while (left < len(line)):
        substring = line[left:left + 4]
        if substring[1].isdigit():
            break;
        if not substring.isspace():
            rows[index].append(substring[1])
        left += 4
        index += 1
for line in commands.splitlines():
    moves = line.split(" ")
    moves = [eval(x) for x in moves]
    sliced = rows[moves[1] - 1][0:moves[0]]
    rows[moves[1] - 1] = rows[moves[1] - 1][moves[0]:]
    rows[moves[2] - 1] = sliced[::-1] + rows[moves[2] - 1]

print("Star 1:", end= " ")
for row in rows:
    print(row[0], end="")
print("\n")

# Star 2
"""
Notes:

"""
rows = []
first = True
for line in test.splitlines():
    if first:
        for x in range(len(line)//4 + 1):
            rows.append([])
        first = False
    left = 0
    index = 0
    while (left < len(line)):
        substring = line[left:left + 4]
        if substring[1].isdigit():
            break;
        if not substring.isspace():
            rows[index].append(substring[1])
        left += 4
        index += 1
for line in commands.splitlines():
    moves = line.split(" ")
    moves = [eval(x) for x in moves]
    sliced = rows[moves[1] - 1][0:moves[0]]
    rows[moves[1] - 1] = rows[moves[1] - 1][moves[0]:]
    rows[moves[2] - 1] = sliced + rows[moves[2] - 1] # only difference from Star 1

print("Star 2:", end= " ")
for row in rows:
    print(row[0], end="")
print("\n")


