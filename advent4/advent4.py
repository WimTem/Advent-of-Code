#get file object
f = open("input.txt", "r")

temp = []
with open('input.txt') as f:
    for line in f:
        temp.append(line.split(" "))
    temp.append(["\n"])
# remove \n
def n(x):
    t = ""
    for i in x:
        if i != "\n":
            t += i
    return t

for i in temp:
    for j in range(len(i)):
        i[j] = n(i[j])

result, dummy = [], []


for i in temp:
    for j in i:
        if len(j) > 1:
            dummy.append(j)
        else:
            result.append(dummy)
            dummy =  []


def byr(x):
    if len(x) == 4:
        if int(x) >= 1920:
            if int(x) <= 2002:
                return 1
    return 0

def iyr(x):
    if len(x) == 4:
        if int(x) >= 2010:
            if int(x) <= 2020:
                return 1
    return 0

def eyr(x):
    if len(x) == 4:
        if int(x) >= 2020:
            if int(x) <= 2030:
                return 1
    return 0
def hgt(x):
    if x[-2:] == "cm":
        if int(x[:-2]) >= 150:
            if int(x[:-2]) <= 193:
                return 1
    elif x[-2:] == "in":
        if int(x[:-2]) >= 59:
            if int(x[:-2]) <= 76:
                return 1
    return 0

def hcl(x):
    if len(x) == 0:
        return 0
    test = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    if x[0] == "#":
        if len(x[1:]) == 6:
            for i in x[1:]:
                if i not in test:
                    return 0
            return 1
    return 0

def ecl(x):
    if x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return 1
    return 0

def pid(x):
    test = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    if len(x) == 9:
        for i in x:
            # ?
            if i not in test:
                return 0
        return 1
    return 0


field = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
x, y, z = 0, 0, 0
for i in result:
    t = []
    if len(i) < 7:
        x += 1
    elif len(i) == 7:
        for j in i:
            t.append(j[:3])
        if set(t) != set(field):
            x += 1
    if len(i) < 7:
        z += 1
    else:
        temp, y = [], 0
        for j in i:
            if j[:3] != "cid":
                temp.append(j)

        for k in temp:
            if k[:3] == field[0]:
                y += byr(k[4:])
            if k[:3] == field[1]:
                y += iyr(k[4:])
            if k[:3] == field[2]:
                y += eyr(k[4:])
            if k[:3] == field[3]:
                y += hgt(k[4:])
            if k[:3] == field[4]:
                y += hcl(k[4:])
            if k[:3] == field[5]:
                y += ecl(k[4:])
            if k[:3] == field[-1]:
                y += pid(k[4:])
        if y != 7:
            z += 1


print("Invalid Old:",x)
print("Invalid New:", z)
print("Valid Old:",len(result) - x)
print("Valid New:", len(result) - z)
print("Total:",len(result))