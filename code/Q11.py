def is_divisible_by5(item):
    intp = int(item, 2)
    if not intp%5:
        return True
    else:
        return False

x = [i for i in input().split(',')]
print(','.join(filter(is_divisible_by5, x)))
