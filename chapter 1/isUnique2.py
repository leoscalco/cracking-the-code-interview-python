def verifyIsUnique(string):
    if len(string) > 128:
        return False

    char_set = {};
    for eachChar in string:
        val = ord(eachChar) # ascii table
        if val in char_set:
            return False
        char_set[val] = True
    return True

# testCase with the string
testCase = raw_input("Type the word you need to verify: ")

# test to lower, so we don`t have problem with t and T. It`s the same here.
testCase = testCase.lower()

if verifyIsUnique(testCase):
    print "Unique."
else:
    print "Not unique."