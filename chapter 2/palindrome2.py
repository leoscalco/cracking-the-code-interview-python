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
def AllSequence(node):
    while(node != None):
        print node.value
        node = node.next

def isPalindrome(head):
    fast = head
    slow = head

    stack = []
    while (fast != None and fast.next != None):
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    # has odd number of elements, skip the middle one
    if (fast != None):
        slow = slow.next

    while(slow != None):
        top = stack.pop()
        if (top != slow.value):
            return False
        slow = slow.next
    return True

print isPalindrome(node1)
