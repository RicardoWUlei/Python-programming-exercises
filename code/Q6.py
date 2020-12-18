import math

def formula(D):
    C = 50
    H = 30
    return str(int(round(math.sqrt((2*C*float(D)/H)))))

seq = input()
result = [formula(x) for x in seq.split(',')]
print(','.join(result))