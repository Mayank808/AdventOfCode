from test import test

# Star 1
"""
Notes:

"""
res = 0
for line in test.splitlines():
    chars = line.replace("-", ",").split(",")
    processed = [eval(x) for x in chars]
    if processed[2] <= processed[0] and processed[1] <= processed[3]:
        res += 1
    elif processed[0] <= processed[2] and processed[3] <= processed[1]:
        res += 1

print("Star 1: ", res)


# Star 2
"""
Notes:

"""
res = 0
for line in test.splitlines():
    chars = line.replace("-", ",").split(",")
    processed = [eval(x) for x in chars]
    if processed[2] <= processed[0] and processed[1] <= processed[3]:
        res += 1
    elif processed[0] <= processed[2] and processed[3] <= processed[1]:
        res += 1
    elif processed[2] <= processed[1] and processed[0] <= processed[3]:
        res += 1 

print("Star 2: ", res)

