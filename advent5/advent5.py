f = open("input.txt", "r")

temp = []
with open('input.txt') as f:
    for line in f:
        temp.append(line[:-1])

result = []
for i in range(len(temp)):
    result.append(list(temp[i]))

data = []

def ltos(x):
    s = ""
    for i in x:
        s += i
    return s

x1, x2 = ["0","0","0","0","0","0","0"], ["0", "0", "0"]
y1, y2 = 0, 0
data = []
for i in range(len(result)):
    x1, x2 = ["0","0","0","0","0","0","0"], ["0", "0", "0"]
    for j in range(7):
        if result[i][j] == 'B':
            x1[j] = "1"
    y1 = int(ltos(x1), 2)

    for k in range(7, 10):
        if result[i][k] == "R":
            x2[k-7] = "1"
    y2 = int(ltos(x2), 2)
    data.append(y1*8 + y2)

print("Max boarding pass:", max(data))

x1, x2 = ["0","0","0","0","0","0","0"], ["0", "0", "0"]
y1, y2 = 0, 0

import numpy as np

seat = np.zeros((len(result), 8))
for i in range(len(result)):
    x1, x2 = ["0","0","0","0","0","0","0"], ["0", "0", "0"]
    for j in range(7):
        if result[i][j] == 'B':
            x1[j] = "1"
    y1 = int(ltos(x1), 2)

    for k in range(7, 10):
        if result[i][k] == "R":
            x2[k-7] = "1"
    y2 = int(ltos(x2), 2)
    seat[y1, y2] = 1

for i in range(seat.shape[0]):
    if sum(seat[i-1,:]) == 8:
        if sum(seat[i, :]) == 7:
            print(i, seat[i, :])
            break

print("ID:", 84*8+4)
