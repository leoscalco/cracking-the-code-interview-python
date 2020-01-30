class MyStack:
    class Node:
        def __init__(self, val):
            self.value = val
            self.next = None

    def __init__(self, value, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = self.Node(value)

    def isFull(self):
        return self.capacity == self.size

    def pop(self):
        if (self.top.value == None):
            self.size -=1
            item = self.top.data
            self.top = self.top.next
            return item

    def push(self, item):
        self.size +=1
        t = self.Node(item)
        t.next = self.top
        self.top = t

    def peek(self):
        if (self.top.value == None):
            print "top = None"
        return self.top

    def isEmpty(self):
        return self.top == None

class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def getLastStack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1]

    def push(self, v):
        last = self.getLastStack()
        if last != None and not last.isFull():
            print "here"
            last.push(v)
        else:
            print "there"
            stack = MyStack(v, self.capacity)
            self.stacks.append(stack)

    def pop(self):
        last = self.getLastStack()
        if last == None:
            print "empty stack"
        v = last.pop()
        if last.size() == 0:
            self.stacks.pop()
        return v

mySet = SetOfStacks(5)
mySet.push(1)
mySet.push(4)
mySet.push(5)
mySet.push(6)
mySet.push(2)
mySet.push(7)
for a in mySet.stacks:
    print a.top.value