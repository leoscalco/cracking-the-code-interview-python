def insertCharAt(word, char, i):
    return word[0:i] + char + word[i:len(word)]

def getPerms(hash, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix)
        return

    for c in hash:
        count = hash[c]
        if count >= 0:
            hash[c] = count - 1
            print "prefix: " + prefix
            print "c: " + c
            getPerms(hash, prefix + c, remaining - 1, result)
            hash[c] = count

def buildFreqTable(string):
    map = {}
    for c in string:
        if c not in map:
            map[c] = 0
        else:
            map[c] += 1
    return map

def printPerms(string):
    result = []
    hash = buildFreqTable(string)
    getPerms(hash, "", len(string), result)
    return result

print printPerms("leo")