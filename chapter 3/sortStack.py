class MyStack:
    class Node:
        def __init__(self, val):
            self.value = val
            self.next = None

    def __init__(self, value):
        # if value != None:
        self.top = self.Node(value)

    def pop(self):
        if (self.top.value != None):
            item = self.top.value
            self.top = self.top.next
            return item

    def push(self, item):
        t = self.Node(item)
        t.next = self.top
        self.top = t

    def peek(self):
        if (self.top.value == None):
            print "top = None"
        return self.top.value

    def isEmpty(self):
        return self.top == None

def sort(s):
    r = MyStack(None)
    while(not s.isEmpty()):
        tmp = s.pop()
        while(not r.isEmpty() and r.peek() > tmp):
            s.push(r.pop())
        r.push(tmp)

    while(not r.isEmpty()):
        s.push(r.pop())


mystack1 = MyStack(5)
mystack1.push(10)
mystack1.push(1)
mystack1.push(66)
mystack1.push(65)
mystack1.push(3)

sort(mystack1)
# mystack1.pop()
# print mystack1.peek()


