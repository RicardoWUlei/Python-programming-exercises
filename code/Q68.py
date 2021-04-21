def evenNumGenerator(n):
    i = 0
    while i <= n:
        if i%2 == 0:
            yield i
        i += 1

n = int(input())
result = []
for i in evenNumGenerator(n):
    result.append(str(i))
print(",".join(result))