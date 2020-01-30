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

def weaveLists(first, second, results, prefix):
    if len(first) == 0 or len(second) == 0:
        result = prefix[:]
        result.extend(first)
        result.extend(second)
        results.append(result)
        return

    headFirst = first.pop(0)
    prefix.append(headFirst)
    weaveLists(first, second, results, prefix)
    prefix.pop()
    first.insert(0, headFirst)

    headSecond = second.pop(0)
    prefix.append(headSecond)
    weaveLists(first, second, results, prefix)
    prefix.pop()
    second.insert(0, headSecond)

def allSequences(node):
    result = []
    if node == None:
        result.append([])
        return result

    prefix = []
    prefix.append(node.value)

    leftSeq = allSequences(node.left)
    rightSeq = allSequences(node.right)

    for left in leftSeq:
        for right in rightSeq:
            weaved = []
            weaveLists(left, right, weaved, prefix)
            result.extend(weaved)

    return result

tree = generateTree(arr, 0, len(arr)-1)
print allSequences(tree)