def invalidDivision():
    return 5/0

try:
    invalidDivision()
except ZeroDivisionError as e:
    print("Get a zero division!", e)