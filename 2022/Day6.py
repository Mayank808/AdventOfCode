from test import test

# Star 1
"""
Notes:
    Sliding Window Question
    Window Size = 4
    Every time we add a new letter in the window we see if the string is unique
    If unique the index of the new letter is the answer
"""
left = 0
right = 0
seen = {}
while (left <= right < len(test)):
    if test[right] in seen:
        left = max(seen[test[right]] + 1, left)
    if right - left + 1 == 4:
        break
    seen[test[right]] = right
    right += 1

print("Star 1: ", right + 1)

# Star 2
"""
Notes:

"""
res = 0
left = 0
right = 0
seen = {}
while (left <= right < len(test)):
    if test[right] in seen:
        left = max(seen[test[right]] + 1, left)
    if right - left + 1 == 14: # only difference
        break
    seen[test[right]] = right
    right += 1

print("Star 2: ", right + 1)

