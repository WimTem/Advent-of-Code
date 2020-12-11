import numpy as np
X = np.zeros((323,31), dtype=int)
x = 0
result = np.zeros(5, dtype=int)

#get file object
f = open("input.txt", "r")

with open('input.txt') as f:
    for line in f:
        for i in range(len(line)):
            if line[i] == "#":
                X[x, i] = 1
        x += 1

result[0] = sum(X[i, i % 31] for i in range(323))
result[1] = sum(X[i, (3*i) % 31] for i in range(323))
result[2] = sum(X[i, (5*i) % 31] for i in range(323))
result[3] = sum(X[i, (7*i) % 31] for i in range(323))
result[4] = sum(X[::2,:][i, i % 31] for i in range(int(323/2)))
print(result)
print(np.product(result))
print(67*299*67*71*38)

