string = raw_input()
string2 = raw_input()
d = {}

counterChanges = 0

for char in string:
    if not char in d:
        d[char] = 1
    else:
        d[char]+=1

for char in string2:
    if char in d:
        d[char]-=1
        if d[char] < 0:
            counterChanges+=1
    else:
        counterChanges+=1

# counterChanges += abs(len(string) - len(string2))
print counterChanges <= 1