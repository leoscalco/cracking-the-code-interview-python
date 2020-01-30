arr = [1, 4, 5, 6, 7, 12, 15, 25, 26]
arr2 = [1, 4, 5]

class Node:
    def __init__(self, value):
        self.value = value
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

def getOrder(node, sb):
    if (node == None):
        # if (node.left != None or node.right != None):
        sb.append("X") # NULL INDICATOR
        return
    # pre-order
    sb.append(str(node.value) + " ") # add root]
    getOrder(node.left, sb) # add left
    getOrder(node.right, sb) # add left

def containsTree(t1, t2):
    string1 = []
    string2 = []
    getOrder(t1, string1)
    getOrder(t2, string2)
    string1 = ''.join(string1[0:-2])
    string2 = ''.join(string2[0:-2])
    print string1
    print string2
    return string1.find(string2) != -1

tree = generateTree(arr, 0, len(arr)-1)
tree2 = generateTree(arr2, 0, len(arr2)-1)

print containsTree(tree, tree2)