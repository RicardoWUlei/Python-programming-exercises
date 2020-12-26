result = filter(lambda x:int(x) % 2 == 1, input().split(','))
print(','.join(result))