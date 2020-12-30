import math

count = [0 for i in range(4)]
while True:
    move = input()
    if not move:
        break
    moves = move.split(" ")
    if moves[0] == "UP":
        count[0] += int(moves[1])
    elif moves[0] == "DOWN":
        count[1] += int(moves[1])
    elif moves[0] == "LEFT":
        count[2] += int(moves[1])
    else:
        count[3] += int(moves[1])

diff_y = count[0] - count[1]
diff_x = count[2] - count[3]
print(round(math.sqrt(diff_x**2+diff_y**2)))