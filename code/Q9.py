L = []
while True:
    s = input()
    if s:
        L.append(s)
    else:
        break

L = list(map(str.upper, L))
for i in L:
    print(i)