import numpy as np
#get file object
f = open("input.txt", "r")

X = np.zeros((323,31), dtype=int)
data = np.zeros((323, 0), dtype=int)
x = 0
result = np.zeros(5, dtype=int)
traj = np.zeros((5,2), dtype=int)
traj[0, :] = [1, 1]
traj[1, :] = [3, 1]
traj[2, :] = [5, 1]
traj[3, :] = [7, 1]
traj[4, :] = [1, 2]
with open('input.txt') as f:
    for line in f:
        for i in range(len(line)):
            if line[i] == "#":
                X[x, i] = 1
        x += 1

for i in range(10):
    data = np.concatenate((data, X), axis=1)


data = np.concatenate((data, X[:,:13]), axis=1)

n = len(data[::2,0])
result[0] = sum(data[i,i] for i in range(323))
result[1] = sum(data[i, (3*i) % 322] for i in range(323))
result[2] = sum(data[i, (5*i) % 322] for i in range(323))
result[3] = sum(data[i, (7*i) % 322] for i in range(323))
ffs = data[::2,:]
result[4] = sum(ffs[i, i] for i in range(len(ffs)))
print(result)

print(np.product(result))
