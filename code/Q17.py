balance = 0
while True:
    s = input()
    if not s:
        break
    input_1 = s.split(' ')
    if len(input_1) < 2:
        break
    if input_1[0] == 'D':
        balance += int(input_1[1])
    if input_1[0] == 'W':
        balance -= int(input_1[1])
    
print(balance)
