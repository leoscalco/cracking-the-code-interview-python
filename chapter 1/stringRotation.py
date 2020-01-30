def isSubstring(s1, s2):
    if s1 in (s2+s2):
        return True
    return False


string1 = raw_input()
string2 = raw_input()

print isSubstring(string1, string2)