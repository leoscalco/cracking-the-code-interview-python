import numpy as np
class FixedMultStack:

    def __init__(self, stackSize):
        self.numberOfStacks = 3
        self.stackCapacity = stackSize
        self.values = np.zeros(stackSize * self.numberOfStacks)
        self.sizes = np.zeros(self.numberOfStacks)

    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.stackCapacity

    def indexOfTop(self, stackNum):
        offSet = stackNum * self.stackCapacity
        size = int(self.sizes[stackNum])
        return (offSet + size - 1)

    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0

    # push
    def push(self, stackNum, value):
        if self.isFull(stackNum):
            print "stack full"

        self.sizes[stackNum]+=1
        self.values[self.indexOfTop(stackNum)] = value

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            print "stack empty"

        topIndex = self.indexOfTop(stackNum)
        value = self.values[topIndex]
        self.values[topIndex] = 0
        self.sizes[stackNum]-=1
        return value

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            print "stack empty"

        return self.values[self.indexOfTop(stackNum)]

arr = [2, 41, 4, 5, 1, 2, 2, 4, 6, 88]

stack = FixedMultStack(4)

for i, a in enumerate(arr):
    if i < len(arr) / 3 + 1:
        stack.push(0, a)
    elif i < len(arr) / 3 * 2 + 1:
        stack.push(1, a)
    else:
        stack.push(2, a)

print stack.peek(0)

