# def magicSlow(arr):
#     for i in xrange(len(arr)):
#         if v[i] == i:
#             return i

#     return -1

def magicFast(arr, s, e):
    if s > e:
        return -1

    middle = (s+e) / 2
    if arr[middle] == middle:
        return middle

    # search left
    leftIndex = min(middle - 1, arr[middle])
    left = magicFast(arr, s, leftIndex)
    if left >= 0:
        return left

    # search right
    rightIndex = max(middle + 1, arr[middle])
    right = magicFast(arr, rightIndex, e)

    return right

def startMagicFast(arr):
    return magicFast(arr, 0, len(arr)-1)

arr = [-1, 1, 5]
print startMagicFast(arr)