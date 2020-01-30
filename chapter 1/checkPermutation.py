# testCase with the string
stringA = raw_input("Type the word you need to verify: ")
stringB = raw_input("Type the word you need to verify: ")

hashA = {}
# hashB = {}

aux = stringA
# aux2 = stringB
for i in  xrange(len(stringA)):
    hashA[aux] = i
    # hashB[aux2] = i
    aux = aux[1:] + aux[0]
    # aux2 = aux2[1:] + aux2[0]


if stringB in hashA:
    print "Yeah baby!"
else:
    print "No baby!"