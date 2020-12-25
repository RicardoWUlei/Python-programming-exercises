x = input()
print("UPPER CASE", len(list(filter(str.isupper, x))))
print("LOWER CASE", len(list(filter(str.islower, x))))