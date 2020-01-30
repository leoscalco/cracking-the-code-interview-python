def verifyIsUnique(h):
    for k in h:
        if h[k] > 1:
            return "Not unique."
    return "Unique."

# testCase with the string
testCase = raw_input("Type the word you need to verify: ")

# dict/hash init
d = {}

# test to lower, so we don`t have problem with t and T. It`s the same here.
testCase = testCase.lower()

# hashmap in python
for t in testCase:
    if t in d:
        d[t] = d[t] + 1
    else:
        d[t] = 1

print verifyIsUnique(d)