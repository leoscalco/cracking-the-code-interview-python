class MyStack:
    class Node:
        def __init__(self, val, min_):
            self.value = val
            self.min = min_
            self.next = None

    def __init__(self, value):
        self.top = self.Node(value)

    def pop(self):
        if (self.top.value == None):
            item = self.top.data
            self.top = self.top.next
            return item

    def push(self, item):
        t = self.Node(item)
        t.next = self.top
        self.top = t

    def peek(self):
        if (self.top.value == None):
            print "top = None"
        return self.top

    def isEmpty(self):
        return top == None