h, m = map(int, input().split())
add = int(input())

m += add

if m < 60:
    pass
elif m % 60 == 0:
    h += m // 60
    m = 0
    if h > 23:
        h = h % 24
else:
#if summed is way over 60
    h += m // 60
    m = m % 60
    if h > 23:
        h = h % 24
        
print(h, m)