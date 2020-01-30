from LinkedList import Node

node1 = Node(7)
node2 = Node(1)
node3 = Node(6)
node4 = Node(1)
node5 = Node(7)
# node6 = Node(7)


# node5.SetNext(node6)
node4.SetNext(node5)
node3.SetNext(node4)
node2.SetNext(node3)
node1.SetNext(node2)

# node1.printAllSequence()
def AllSequence(node):
    while(node != None):
        print node.value
        node = node.next

def isPalindrome(node, middle):
    stack = []
    head = node
    counter = 0
    while (node != None):
        if (counter < middle):
            stack.append(node.value)
        else:
            if stack[-1] == node.value:
                stack.pop()
        print stack
        counter += 1
        node = node.next

    if (len(stack) == 0):
        return True
    else:
        return False

print isPalindrome(node1, 2)
