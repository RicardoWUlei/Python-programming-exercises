import re

def is_valid(item):
    if len(item) < 6 or len(item) > 12:
        return False
    if not re.search("[a-z]", item):
        return False
    if not re.search("[0-9]", item):
        return False
    if not re.search("[A-Z]", item):
        return False
    if not re.search("[$#@]", item):
        return False
    return True

result = filter(is_valid, input().split(','))
print(','.join(result))