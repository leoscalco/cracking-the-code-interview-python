from LinkedList import Node

node1 = Node(12)
# node1.SetNext(Node(15).SetNext(Node(1)))
node2 = Node(15)
node3 = Node(1)

node2.SetNext(node3)
node1.SetNext(node2)

def printKthToLast(head, k):
    if head == None:
        return 0
    index = printKthToLast(head.next, k) + 1
    if index <= k:
        print "%dth to last node is %d" % (index, head.value)
    return index

printKthToLast(node1, 2)