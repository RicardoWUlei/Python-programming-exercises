ls = []
while True:
    x = input()
    ## No input
    if not x:
        break
    info = x.split(',')
    ls.append((info[0],info[1],info[2]))

print(sorted(ls, key=lambda s: (s[0], s[1], s[2])))