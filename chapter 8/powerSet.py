def getSubSets(set, index):
    allSubsets = []
    if len(set) == index:
        allSubsets.append([])
    else:
        allSubsets = getSubSets(set, index+1)
        item = set[index]
        moreSubSets = []
        for subset in allSubsets:
            newSubSet = []
            newSubSet.extend(subset)
            newSubSet.append(item)
            moreSubSets.append(newSubSet)
        allSubsets.extend(moreSubSets)
    return allSubsets


set_ = ['a', 'b', 'c']
print getSubSets(set_, 0)