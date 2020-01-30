class MyStack:
    class Node:
        def __init__(self, val, min_):
            self.value = val
            self.min = min_
            self.next = None

    def __init__(self, value):
        self.top = self.Node(value, value)

    def min(self):
        if (self.isEmpty()):
            return 99999999 # error
        else:
            return self.peek().min

    def pop(self):
        if (self.top.value == None):
            item = self.top.data
            self.top = self.top.next
            return item

    def push(self, item):
        newMin = item if item < self.min() else self.min()
        t = self.Node(item, newMin)
        t.next = self.top
        self.top = t

    def peek(self):
        if (self.top.value == None):
            print "top = None"
        return self.top

    def isEmpty(self):
        return self.top == None

stack = MyStack(5)
stack.push(10)
print stack.peek().value, stack.peek().min