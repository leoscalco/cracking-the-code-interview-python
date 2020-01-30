string = "leo"

def insertCharAt(word, char, i):
    return word[0:i] + char + word[i:len(word)]

def getPerms(string):
    if string == None:
        return None
    permutations = []
    if len(string) == 0:
        permutations.append("")
        return permutations

    first = string[0]
    remainder = string[1:len(string)]
    words = getPerms(remainder)
    for word in words:
        for j in xrange(len(word)+1):
            s = insertCharAt(word, first, j)
            permutations.append(s)
    return permutations

print getPerms(string)