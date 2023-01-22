a = list(map(int, input().split()))
c = a.count(a[0])
d = a.count(a[1])
if c == 3:
    print(a[0]*1000+10000)
elif c == 2 or d == 2:
    print(a[0]*100+1000 if c == 2 else a[1]*100+1000)
else:
    print(max(a)*100)