def compute_value(n):
    """
    Compute the value of f recursively.
    """
    if n == 0:
        return 0
    else:
        return 100 + compute_value(n-1)

n = int(input())
print(compute_value(n))