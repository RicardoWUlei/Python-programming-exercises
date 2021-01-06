def printLonger(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 < len2:
        print(s2)
    elif len1 > len2:
        print(s1)
    else:
        print(s1)
        print(s2)

printLonger('12', '123')