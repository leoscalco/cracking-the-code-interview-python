string = raw_input()

positionSpace = []
for i in xrange(len(string)):
    if string[i] == ' ':
        positionSpace.append(i)

for pos in positionSpace:
    aux = string[0:pos] + "%20" + string[pos+1:]

print aux