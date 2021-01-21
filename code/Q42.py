def printTuple():
    tuple1 = tuple([x for x in range(1,11)])
    print(tuple1[:len(tuple1)//2])
    print(tuple1[len(tuple1)//2:])

printTuple()