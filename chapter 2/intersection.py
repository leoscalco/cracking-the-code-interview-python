from LinkedList import Node

node1 = Node(7)
node2 = Node(1)
node3 = Node(6)
# node4 = Node(7)
node4 = Node(99999)
node5 = Node(7)
# node6 = Node(7)

nodeA = Node(88)
nodeB = Node(99)
nodeC = Node(884)

# node5.SetNext(node6)
# node5.SetNext(node6)
node4.SetNext(node5)
node3.SetNext(node4)
node2.SetNext(node3)
node1.SetNext(node2)

nodeC.SetNext(node4)
nodeB.SetNext(nodeC)
nodeA.SetNext(nodeB)

class Result:
    def __init__(self, tail, size):
        self.tail = tail
        self.size = size

def getTailAndSize(linkedList):
    if linkedList == None:
        return None

    size = 1
    current = linkedList
    while current != None:
        size += 1
        current = current.next
    return Result(current, size)

def getKthNode(head, k):
    current = head
    while k > 0 and current != None:
        current = current.next
        k -= 1
    return current

def findIntersection(a, b):
    if (a == None or b == None):
        return None

    result1 = getTailAndSize(a)
    result2 = getTailAndSize(b)

    if(result1.tail != result2.tail):
        return None

    shorter = a if result1.size > result2.size else b
    longer = b if result2.size > result1.size else a

    longer = getKthNode(longer, abs(result2.size - result1.size))

    while(shorter != longer):
        shorter = shorter.next
        longer = longer.next

    return longer

print findIntersection(node1, nodeA).value
