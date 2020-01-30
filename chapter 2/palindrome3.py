from LinkedList import Node

node1 = Node(7)
node2 = Node(1)
node3 = Node(6)
# node4 = Node(7)
node4 = Node(1)
node5 = Node(7)
# node6 = Node(7)


# node5.SetNext(node6)
# node5.SetNext(node6)
node4.SetNext(node5)
node3.SetNext(node4)
node2.SetNext(node3)
node1.SetNext(node2)

# node1.printAllSequence()
def isPalindromeRecurse(head, length):
    if head == None or length <= 0:
        # even number of nodes
        return head, True
    elif length == 1:
        return head.next, True

    node, boolean = isPalindromeRecurse(head.next, length - 2) # going to half

    if not boolean or node == None:
        return node, boolean

    boolean = head.value == node.value
    node = node.next
    return node, boolean

def lengthOfList(node):
    size = 0
    while (node != None):
        size+=1
        node = node.next
    return size

def isPalindrome(head):
    length = lengthOfList(head)
    node, boolean = isPalindromeRecurse(head, length)
    return boolean

print isPalindrome(node1)
