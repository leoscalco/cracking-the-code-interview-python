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


def incrementHashTable(hash, key, delta):
    newCount = hash.get(key, 0) + delta
    if newCount == 0:
        hash.pop(key, None)
    else:
        hash[key] = newCount

def countPathsWithSum(node, targetSum, runningSum, pathCount):
    if node == None:
        return 0

    runningSum+=node.value
    sum = runningSum - targetSum
    totalPaths = pathCount.get(sum, 0)
    if (runningSum == targetSum):
        totalPaths+=1

    incrementHashTable(pathCount, runningSum, 1)
    totalPaths += countPathsWithSum(node.left, targetSum, runningSum, pathCount)
    totalPaths += countPathsWithSum(node.right, targetSum, runningSum, pathCount)

    incrementHashTable(pathCount, runningSum, -1)
    return totalPaths

print countPathsWithSum(tree, 51, 0, {})