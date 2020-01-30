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

def validateBST(treeNode, min, max):
    if (treeNode == None):
        return True

    if (min != None and treeNode.name <= min) or (max != None and treeNode.name > max):
        return False

    if (not validateBST(treeNode.left, min, treeNode.name)
        or (not validateBST(treeNode.right, treeNode.name, max))):
        return False

    return True

# tree = generateTree(arr, 0, len(arr)-1)
tree = Node(5)
tree.left = Node(45)
tree.left.left = Node(12)


print validateBST(tree, None, None)

# print d
