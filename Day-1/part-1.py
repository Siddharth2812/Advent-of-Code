n = int(input())
count = 0
while True:
    try:
        m = int(input())
        if m>n:
            count+=1
        n = m
    except:
        break
print(count)
