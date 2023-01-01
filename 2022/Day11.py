from test import test
import math
# Star 1
"""
Notes:
    Graph style problem
    Each monkey is a node and the worrys are being moved based on the operations
    Create a monkey class to handle functionalty
"""
class Monkey:
    def __init__(self, num):
        self.num = num
        self.items = []
        self.op = []
        self.test = 0
        self.tThrowTo = -1
        self.fThrowTo = -1
        self.inspected = 0
    
    def __str__(self) -> str:
        return "Monkey " + str(self.num) + "\nInspects: " + str(self.inspected) + "\nItems: " + str(self.items) + "\nOperations: " + str(self.op) + "\nTest: " + str(self.test) + " True " + str(self.tThrowTo) + " False " + str(self.fThrowTo)
       
    def addItems(self, items):
        for x in items:
            self.items.append(int(x))
    
    def addOp(self, op):
        self.op = op
    
    def addTest(self, test, tThrowTo, fThrowTo):
        self.test = test
        self.tThrowTo = tThrowTo
        self.fThrowTo = fThrowTo
    
    def __determineOp(self, op, item):
        val = 0
        if op == "old":
            val = item
        else:
            val = int(op)
        return val
    
    def __applyOp(self, item):
        leftS = self.__determineOp(self.op[0], item)
        rightS = self.__determineOp(self.op[2], item)
        if self.op[1] == "+":
            return leftS + rightS
        return leftS * rightS
    
    def __test(self, worry):
        if worry % self.test == 0:
            return self.tThrowTo
        return self.fThrowTo
        
    # handles inspection of all items and returns a tuple of array
    # array of tuples are as follows [(send item i to monkey x, new worry for item i,), ... ]
    def inspect(self, factor = -1):
        moves = []
        for worry in self.items:
            newWorry = self.__applyOp(worry) # // 3 divide by for part 1
            newWorry = newWorry % factor if factor != -1 else newWorry // 3 
            sendTo = self.__test(newWorry)
            moves.append((sendTo, newWorry))
            self.inspected += 1        
        self.items = []
        return moves   
    
    def appendItem(self, item):
        self.items.append(item) 
    
    def getInspects(self):
        return self.inspected
    
    def getTest(self):
        return self.test
        

"""
Sample Input for One Monkey: 
    Monkey 0:
        Starting items: 79, 98
        Operation: new = old * 19
        Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3
            testing
"""
def getMonkeyCollection(test):
    monkeys = []
    head = []
    for line in test.splitlines():
        if not line:
            continue
        head.append(line)
        if len(head) == 6:
            newM = Monkey(int(head[0].split(' ')[1][0]))
            newM.addItems(head[1].split(":")[1].split(","))
            newM.addOp(head[2].split("= ")[1].split(" "))
            test = int(head[3].split("by ")[1])
            trueThrow = int(head[4].split("monkey ")[1])
            falseThrow = int(head[5].split("monkey ")[1])
            newM.addTest(test, trueThrow, falseThrow)
            monkeys.append(newM)
            head = []
    return monkeys


monkeys = getMonkeyCollection(test)         
res = 0

for i in range(20):
    for monkey in monkeys:
        moves = monkey.inspect() 
        for move in moves:
            monkeys[move[0]].appendItem(move[1])

interactions = []
for monkey in monkeys:
    interactions.append(monkey.getInspects())
interactions.sort()
res = interactions[-1] * interactions[-2]
print("Star 1: ", res)

# Star 2
"""
Notes:

"""
res = 0
monkeys = getMonkeyCollection(test)         
factor = 1

# instead of dividing by 3 we are not modding values by factor to maintain divisibility 
# between values for monkeys and also not allowing the worry value to be very large numbers
for monkey in monkeys:
    factor *= monkey.getTest()

for i in range(10000):
    for monkey in monkeys:
        moves = monkey.inspect(factor) 
        for move in moves:
            monkeys[move[0]].appendItem(move[1])

interactions = []
for monkey in monkeys:
    interactions.append(monkey.getInspects())
interactions.sort()
res = interactions[-1] * interactions[-2]
print("Star 2: ", res)

