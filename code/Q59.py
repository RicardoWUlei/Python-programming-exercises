import re
raw_input = input("Type in your email addreass: ")
regex = re.compile(r"(\w*)@(\w*)\.com")
result = regex.match(raw_input)
print(result.group(2))