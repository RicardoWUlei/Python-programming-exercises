def printDict():
    dict1 = {x:x**2 for x in range(1,21)}
    for k in dict1.keys():
        print(dict1[k])

printDict()