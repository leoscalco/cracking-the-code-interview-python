from LinkedList import Node

node1 = Node(3)
node2 = Node(5)
node3 = Node(8)
node4 = Node(5)
node5 = Node(10)

node4.SetNext(node5)
node3.SetNext(node4)
node2.SetNext(node3)
node1.SetNext(node2)

# node1.printAllSequence()
def AllSequence(node):
    while(node != None):
        print node.value
        node = node.next

def partition(node, k=5):
    head = node
    tail = node

    while node != None:
        next = node.next
        if (node.value < k):
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None
    return head

# AllSequence(node1)
answer = partition(node1, 8)
# AllSequence(partition(node1, 5))
AllSequence(answer)
