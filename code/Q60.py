import re
raw_input = input()
print(re.findall(r"\d+", raw_input))