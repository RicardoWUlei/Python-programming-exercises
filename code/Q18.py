def is_valid(item):
    if len(item) < 6 or len(item) > 12:
        return False
    if len(list(filter(str.islower, item))) < 1:
        return False
    if len(list(filter(str.isupper, item))) < 1:
        return False
    if len(list(filter(str.isnumeric, item))) < 1:
        return False
    

result = filter(is_valid, input().split(','))
print(','.join(result))