t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        floor = h
        walk = int(n / h)
    else:
        walk = int(n // h + 1)
        floor = n % h
    print(floor * 100 + walk)
