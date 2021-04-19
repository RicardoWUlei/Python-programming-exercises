import re
regex = re.compile(r"(.*)@.*\.com")
input_msg = input("Type email address: ")
result =  regex.match(input_msg)
print(result.group(1))