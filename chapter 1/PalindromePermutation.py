string = raw_input()

d = {}

for char in string:
    if char in d:
        d[char]+=1
    else:
        d[char] = 1

counter = 0
for element in d:
    if d[element] % 2 == 1:
        counter+=1

if counter > 1:
    print "not"
else:
    print "yes"