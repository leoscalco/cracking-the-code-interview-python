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

def getDepthTree(treeNode, d_dict, depth):
    if (treeNode == None):
        return

    if depth not in d_dict:
        d_dict[depth] = [treeNode]
    else:
        d_dict[depth].append(treeNode)

    # print "%d %d" % (depth, treeNode.name)

    getDepthTree(treeNode.left, d_dict, depth+1)
    getDepthTree(treeNode.right, d_dict, depth+1)


tree = generateTree(arr, 0, len(arr)-1)
d = {}
getDepthTree(tree, d, 0)

# print d
