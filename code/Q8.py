x = input()
words = [i for i in x.split(',')]
words = sorted(words)
print(','.join(words))