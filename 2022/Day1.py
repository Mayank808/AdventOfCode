from test import test

# star 2
cals = []
cur_cal = 0
for line in test.splitlines():
    if line == '':
        cals.append(cur_cal)
        cur_cal = 0
    else:
        cur_cal += int(line)
        
cals.sort(reverse=True)

print("Star 2: ", sum(cals[0:3]))



# star 1
max_cal = 0
for line in test.splitlines():
    if line == '':
        max_cal = max(max_cal, cur_cal)
        cur_cal = 0
    else:
        cur_cal += int(line)
max_cal = max(max_cal, cur_cal)

print("Star 1: ", max_cal)

