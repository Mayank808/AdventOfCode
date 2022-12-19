from test import test
import queue
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
res = 0
rows = []
first = True
for line in test.splitlines():
    if first:
        for x in range(len(line)//4 + 1):
            rows.append(queue.Queue())
        first = False
    left = 0
    index = 0
    while (left < len(line)):
        substring = line[left:left + 4]
        if substring[1].isdigit():
            break;
        if not substring.isspace():
            rows[index].put(substring[1])
        left += 4
        index += 1
for q in rows:
    print(q.get())



print("Star 1: ", res)

# Star 2
"""
Notes:

"""
res = 0


print("Star 2: ", res)

