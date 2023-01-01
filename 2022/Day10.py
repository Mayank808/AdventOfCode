from test import test

# Star 1
"""
Notes:

"""
res = 0
ops = []
for line in test.splitlines():
   ops.append(line.split(' '))
def calcSignalStrength(signal, strength):
    return signal * strength

def isSignal(signal):
    if signal in (20, 60, 100, 140, 180, 220):
        return True
    return False

signal = 0
x = 1
index = 0
while signal <= 220:
    op = ops[index]
    signal += 1
    if isSignal(signal):
        res += calcSignalStrength(signal, x)
    if op[0] == "addx":
        signal += 1
        if isSignal(signal):
            res += calcSignalStrength(signal, x)
        x += int(op[1])
    index += 1
    index = index % len(ops)

print("Star 1: ", res)
# Star 2
"""
Notes:

"""
def isNewRow(signal):
    return (signal % 40 == 0)
def inSpriteRange(drawPos, spritePos):
    return (drawPos >= spritePos and drawPos <= spritePos + 2)
def appendToString(str, signal, x):
    if inSpriteRange(signal % 40, x):
        str += "▦"
    else:
        str += " "
    if isNewRow(signal):
        str += "\n"
    return str
signal = 0
x = 1
index = 0
crt = ""
while signal < 240:
    op = ops[index]
    signal += 1
    crt = appendToString(crt, signal, x)
    if op[0] == "addx":
        signal += 1
        if signal == 241: 
            break
        crt = appendToString(crt, signal, x)
        x += int(op[1])
    index += 1
    index = index % len(ops)
print("Star 2:")
print(crt)
