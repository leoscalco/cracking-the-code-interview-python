def compression(string):
    # O n - SIZE OF STRING
    counter = 1
    compressionList = [string[0]]
    for i in xrange(1, len(string)):
        if string[i-1] == string[i]:
            counter+=1
        else:
            compressionList.append(str(counter))
            compressionList.append(string[i])
            counter=1

    compressionList.append(str(counter))
    aux = ''.join(compressionList)
    if len(string) <= len(aux):
        return string
    return aux

string = raw_input()
print compression(string)
