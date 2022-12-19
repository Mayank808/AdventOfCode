from test import test

# Star 1
"""
Notes:

"""
res = 0
c1 = set()
for line in test.splitlines():
    for item in line[0:(len(line) // 2)]:
        c1.add(item)
    for item in line[len(line) // 2:]:
        if item in c1:
            if item.isupper():
                res += ord(item) - ord('A') + 27
            else: 
                res += ord(item) - ord('a') + 1
            c1.clear()
            break; 

print("Star 1: ", res)

# Star 2
"""
Notes:

"""

res = 0
c1 = set()
c2 = set()
group = 1
for line in test.splitlines():
    if group % 3 == 1:
        for item in line:
            c1.add(item)
    elif group % 3 == 2:
        for item in line:
            c2.add(item)
    else:      
        for item in line:
            if item in c1 and item in c2:
                if item.isupper():
                    res += ord(item) - ord('A') + 27
                else: 
                    res += ord(item) - ord('a') + 1
                c1.clear()
                c2.clear()
                break; 
    group += 1

print("Star 2: ", res)
