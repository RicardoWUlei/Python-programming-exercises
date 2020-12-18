size = input()
x = int(size.split(',')[0])
y = int(size.split(',')[1])
result = [[i*j for i in range(y)] for j in range(x)]
print(result)