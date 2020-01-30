from LinkedList import Node

node1 = Node(12)
# node1.SetNext(Node(15).SetNext(Node(1)))
node2 = Node(15)
node3 = Node(1)

node2.SetNext(node3)
node1.SetNext(node2)

def nthToLastElement(head, k):
    p1 = head
    p2 = head

    for i in xrange(k):
        if p1 == None:
            return None
        p1 = p1.next

    while(p1 != None):
        p1 = p1.next
        p2 = p2.next

    return p2

print nthToLastElement(node1, 2).value