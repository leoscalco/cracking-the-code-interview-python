def isPermutationOfPalindrome(phrase):
    countOdd = 0

    d = {}
    for char in phrase:
        x = ord(char)
        if x != -1:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
            if d[x] % 2 == 1:
                countOdd+=1 # primeira vez todos somam
            else:
                countOdd-=1
    return countOdd <= 1

string = raw_input()
print isPermutationOfPalindrome(string)
