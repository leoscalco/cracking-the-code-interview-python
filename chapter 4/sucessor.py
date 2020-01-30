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
        self.parent = None

    def getChildren(self):
        return self.left, self.right

def generateTree(arr, s, e, parent):
    if s > e:
        return None
    middle = (s + e) / 2
    head = Node(arr[middle])
    head.left = generateTree(arr, s, middle - 1, head)
    head.right = generateTree(arr, middle + 1, e, head)
    head.parent = parent
    return head

def leftMostChild(node):
    if node == None:
        return None

    while node.left != None:
        node = node.left

    return node

def inOrderSucc(node):
    if node == None:
        return None

    if (node.right != None):
        return leftMostChild(node.right)
    else:
        q = node
        x = q.parent
        while x != None and x.left != q: # se ele é o pai direto, ou se ele é o nó head.
            q = x
            x = x.parent
        return x

tree = generateTree(arr, 0, len(arr)-1, None)
print inOrderSucc(tree.left.left).name



# print validateBST(tree, None, None)

# print d
