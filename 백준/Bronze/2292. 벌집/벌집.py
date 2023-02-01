n = int(input())
a, d = 1, 1
while a < n:
    a += 6*d
    d += 1
print(d)