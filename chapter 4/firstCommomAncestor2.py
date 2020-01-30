# arr = [1,2,3,4,6,3,4,5]
arr = [1, 4, 5, 6, 7, 12, 15, 25, 26]

class TreeNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
        self.parent = None


def generateTree(arr, s, e, parent):
    if e < s:
        return None

    middle = (s+e)/2
    head = TreeNode(arr[middle])
    head.parent = parent
    head.left = generateTree(arr, s, middle-1, head)
    head.right = generateTree(arr, middle+1, e, head)

    return head

def depth(node):
    depth = 0
    while node != None:
        node=node.parent
        depth+=1
    return depth

def goUpBy(node, delta):
    while delta > 0 and node != None:
        node = node.parent
        delta -= 1
    return node

def findAncestor(node1, node2):
    delta = depth(node1) - depth(node2)

    first = node2 if delta > 0 else node1
    second = node1 if delta > 0 else node2

    second = goUpBy(second, abs(delta))

    while first != second and first != None and second != None:
        first = first.parent
        second = second.parent

    return None if (first == None or second == None) else first

tree = generateTree(arr, 0, len(arr)-1, None)
print findAncestor(tree.right.left, tree.right.right.right).value
