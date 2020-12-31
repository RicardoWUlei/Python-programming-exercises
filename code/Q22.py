x = input().split(" ")
output = {}
for word in x:
    if word not in output:
        output[word] = 0
    else:
        output[word] += 1
for word in sorted(output, key=lambda x: x[0]):
    print("%s:%s" % (word, output[word]))