arr = [1, 4, 5, 6, 7, 12, 15, 25, 26]

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

tree = generateTree(arr, 0, len(arr)-1)

def countPathWithSumFromNode(node, targetSum, currentSum):
    if node == None:
        return 0

    currentSum += node.value

    totalPaths = 0
    if currentSum == targetSum:
        totalPaths += 1

    totalPaths += countPathWithSumFromNode(node.left, targetSum, currentSum)
    totalPaths += countPathWithSumFromNode(node.right, targetSum, currentSum)
    return totalPaths

def countPathWithSum(root, targetSum):
    if root == None:
        return 0

    pathsFromRoot = countPathWithSumFromNode(root, targetSum, 0)
    pathsOnLeft = countPathWithSum(root.left, targetSum)
    pathsOnRight = countPathWithSum(root.right, targetSum)
    return pathsFromRoot + pathsOnLeft + pathsOnRight

print countPathWithSum(tree, 12)