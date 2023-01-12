a = list(map(int, input().split()))
check = [1, 1, 2, 2, 2, 8]

for i in range(6):
    check[i] -= a[i]
print(*check)
    
