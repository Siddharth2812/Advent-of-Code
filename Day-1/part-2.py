x = ""
l = []
b = []
count = 0
while x != 00000:
    x = int(input())
    l.append(x)
l.remove(00000)
count = 0
for i in range(len(l)-2):
    a = l[i]+l[i+1]+l[i+2]
    b.append(a)
for i in range(len(b)-1):
    if b[i]<b[i+1]:
        count+=1
print(count)
