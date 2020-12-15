def factorial(n) -> int:
    if n==1:
        return 1
    else:
        return factorial(n-1) * n

def factorial_iteration(n) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

x = input() # take in console input
print(factorial_iteration(int(x)))