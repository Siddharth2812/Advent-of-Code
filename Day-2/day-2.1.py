x = ""
l = []
while x != "stop" :
    x = input()
    l.append(x)
l.remove("stop")
u = []
f = []
d = []
for i in range(len(l)):
    if "up " in l[i]:
        u.append((l[i])[3])
    if "forward " in l[i]:
        f.append((l[i])[8])
    if "down " in l[i]:
        d.append((l[i])[5])
f = [int(i) for i in f]
u = [int(i) for i in u]
d = [int(i) for i in d]
a = sum(f)
b = sum(u) - sum(d)
print(-(a*b))
