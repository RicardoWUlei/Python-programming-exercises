def genNumber(n):
    for i in range(n):
        if i % 7 == 0:
            yield i

for i in genNumber(100):
    print(i)