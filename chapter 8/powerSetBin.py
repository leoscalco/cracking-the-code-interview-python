def convertIntToSet(x, set):
    subSet = []
    index = 0
    k = x
    while k  > 0:
        if (k & 1) == 1:
            subSet.append(set[index])
        index+=1
        k >>= 1

    return subSet


def getSubSets2(set):
    allSubSets = []
    max = 1 << len(set)
    for i in xrange(max):
        subSet = convertIntToSet(i, set)
        allSubSets.append(subSet)

    return allSubSets

set_ = ['a', 'b', 'c']
print getSubSets2(set_)