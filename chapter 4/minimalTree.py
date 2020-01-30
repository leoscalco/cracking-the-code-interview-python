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

    print head.name
    if head.left != None:
        print "L %d", head.left.name
    if head.right != None:
        print "R %d", head.right.name
    return head

generateTree(arr, 0, len(arr)-1)
