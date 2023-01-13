a, b = map(int, input().split())
t = 45
b -= 45

#if b is positive
if b >= 0:
    print(a,b)
        
#if b is negative
else:
    b += 60
    a -= 1
    if a < 0:
        a += 24
    print(a,b)