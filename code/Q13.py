x = input()
print("LETTERS", len(list(filter(str.isalpha, x))))
print("LETTERS", len(list(filter(str.isdigit, x))))