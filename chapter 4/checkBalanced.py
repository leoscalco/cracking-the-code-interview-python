import sys
arr = [1, 4, 5, 6, 7, 12, 15, 25, 26]
UNVISITED = 0
VISITED = 1
VISITING = 2

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def getChildren(self):
        return self.left, self.right

def generateTree(arr, s, e):
    if s > e:
        return None
    middle = (s + e) / 2
    head = Node(arr[middle])
    head.left = generateTree(arr, s, middle - 1)
    head.right = generateTree(arr, middle + 1, e)
    return head

def checkBalanced(treeNode):
    if treeNode == None:
        return -1

    checkLeft = checkBalanced(treeNode.left)
    if (checkLeft == -sys.maxint-1):
        return -sys.maxint-1

    checkRight = checkBalanced(treeNode.right)
    if (checkRight == -sys.maxint-1):
        return -sys.maxint-1

    heightDiff = abs(checkLeft - checkRight)
    if (heightDiff > 1):
        return -sys.maxint-1
    else:
        return max(checkLeft, checkRight) + 1 # conta o numero de nos ao mesmo tempo que

tree = generateTree(arr, 0, len(arr)-1)

print checkBalanced(tree)

# print d
