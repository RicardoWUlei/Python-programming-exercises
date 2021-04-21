def compute_value(n):
    result = 0
    for i in range(1, n+1):
        result += i/(i+1)
    return result

x = int(input())
print(compute_value(x))