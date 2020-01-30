def isPermutation(a, b):
    if len(a) != len(b):
        return False

    letters = {}
    for char in a:
        letters[ord(char)]++

    for char in b:
        letters[ord(char)]--
        if letters[ord(char)] < 0:
            return False
    return True

# testCase with the string
stringA = raw_input("Type the word you need to verify: ")
stringB = raw_input("Type the word you need to verify: ")

hashA = {}

if isPermutation:
    print "Yeah"
else:
    print "No"