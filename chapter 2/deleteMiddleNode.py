from LinkedList import Node

node1 = Node(12)
# node1.SetNext(Node(15).SetNext(Node(1)))
node2 = Node(15)
node3 = Node(1)

node2.SetNext(node3)
node1.SetNext(node2)

# node1.printAllSequence()
def AllSequence(node):
    while(node != None):
        print node.value
        node = node.next

# def deleteMiddleNode(node):
#     p1 = node
#     middle = 0
#     while node != None:
#         middle+=1
#         node = node.next
#     middle /= 2
#     count = 0
#     while True:
#         if (count == middle):
#             p1.SetNext((p1.next).next)
#             break;
#         count+=1
#         p1 = p1.next

def deleteMiddleNode(node):
    if node == None and node.next != None:
        return False

    next = node.next
    node.value = next.value
    node.next = next.next
    return True

AllSequence(node1)
deleteMiddleNode(node2)
AllSequence(node1)