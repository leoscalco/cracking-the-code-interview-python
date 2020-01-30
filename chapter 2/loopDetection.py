from LinkedList import Node

node1 = Node(34)
node2 = Node(1)
node3 = Node(6)
# node4 = Node(7)
node4 = Node(1)
node5 = Node(99)
# node6 = Node(7)

# node5.SetNext(node6)
# node5.SetNext(node6)
node5.SetNext(node3)
node4.SetNext(node5)
node3.SetNext(node4)
node2.SetNext(node3)
node1.SetNext(node2)

# nodeC.SetNext(node4)
# nodeB.SetNext(nodeC)
# nodeA.SetNext(nodeB)

def loopDetection(head):
    fast = head
    slow = head

    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if (fast == None or fast.next == None):
        return None

    slow = head
    while(slow != fast):
        slow = slow.next
        fast = fast.next

    return fast

print loopDetection(node1).value
