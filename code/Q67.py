def fib_tabulation(n):
    """
    Calculate Fibonacci sequence with tabulation. 
    """
    if tabulation[n] == -1:
        tabulation[n] = fib_tabulation(n-1) + fib_tabulation(n-2)
        return tabulation[n]
    else:
        return tabulation[n]

n = int(input())
tabulation = [-1 for i in range(n+1)]
## Base cases
tabulation[0] = 0
tabulation[1] = 1
## DP
fib_tabulation(n)
print(','.join(map(str, tabulation)))