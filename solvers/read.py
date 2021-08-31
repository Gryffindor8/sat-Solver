f = open("test.txt", "r")
lines = f.readlines()
_list = []
for k in lines[1:]:
    line1 = k.strip()
    line = line1.split(" ")
    a = [int(j) for j in line[:-1]]
    _list.append(a)
print(_list)

