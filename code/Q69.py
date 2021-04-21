def numGenerator(n):
    i = 0
    while i <= n:
        if i%5==0 and i%7==0:
            yield i
        i += 1

n = int(input())
result = []
for i in numGenerator(n):
    result.append(str(i))
print(",".join(result))