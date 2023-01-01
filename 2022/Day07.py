from test import test
from collections import defaultdict
# Star 1
"""
Notes:
    Build the current file path
    Build a Dictionary that stores the sum of the values for a specific file path
"""
res = 0
curFilePath = []
sizes = defaultdict(int)
for line in test.splitlines():
    line = line.split(' ')
    # user command build file path through this
    if line[0] == '$':
        if line[1] == 'cd':
            # handle change of dir
            if line[2] == '/':
                curFilePath = ['/']
            elif line[2] == '..':
                curFilePath.pop()
            else:
                curFilePath.append(line[2])
    # post ls command
    else:
        if line[0] != "dir":
            fileSize = int(line[0])
            path = ""
            for x in range(len(curFilePath)):
                if x <= 1:
                    sizes[curFilePath[x]] += fileSize
                    path += curFilePath[x]
                else:
                    path += curFilePath[x]
                    sizes[path] += fileSize
for size in sizes.values():
    if size <= 100000:
        res += size
print("Star 1: ", res)

# Star 2
"""
Notes:

"""
res = 0
usedSpace = int(sizes['/'])
haveSpace = 70000000 - usedSpace
reqSpace = 30000000 - haveSpace
# dir_sizes = [x for x in sizes.values()]
# dir_sizes.sort()
min_val = []
for val in sizes.values():
    if int(val) >= reqSpace:
        min_val.append(val)
# print(usedSpace, haveSpace, reqSpace)
print("Star 2: ", min(min_val))

