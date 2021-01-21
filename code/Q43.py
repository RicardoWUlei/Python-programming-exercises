def printEvenNum():
    tuple1 = (1,2,3,4,5,6,7,8,9,10)
    print(tuple(filter(lambda x: x%2==0, tuple1)))

printEvenNum()