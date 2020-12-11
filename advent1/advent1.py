from numpy import loadtxt
lines = loadtxt("input.txt", comments="#", delimiter="\n", unpack=False)


result = []

for i in lines:
    for j in lines:
        if i != j:
            if i+j == 2020:
                print(i,j)
                result.append(i*j)

result2 = []

for i in lines:
    for j in lines:
        for k in lines:
         if i != j and j != k:
             if i+j+k == 2020:
                 print(i,j)
                 result2.append(i*j*k)
print(result2)
