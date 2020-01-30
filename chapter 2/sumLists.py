from LinkedList import Node

node1 = Node(7)
node2 = Node(1)
node3 = Node(6)

node4 = Node(5)
node5 = Node(9)
node6 = Node(2)


node5.SetNext(node6)
node4.SetNext(node5)

node2.SetNext(node3)
node1.SetNext(node2)

# node1.printAllSequence()
def AllSequence(node):
    while(node != None):
        print node.value
        node = node.next

def addLists(l1, l2, carry):
    if (l1 == None and l2 == None and carry == 0):
        return None;

    value = carry
    if (l1 != None):
        value += l1.value
    if(l2 != None):
        value += l2.value

    result = Node(value % 10)

    # recursao
    if(l1 != None or l2 != None):
        more = addLists(None if l1 == None else l1.next,
            None if l2 == None else l2.next,
            1 if value >= 10 else 0)

        result.SetNext(more)

    return result

AllSequence(addLists(node1, node4, 0))
