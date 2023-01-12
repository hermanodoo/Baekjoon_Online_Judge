T = int(input())
summed = list()

for i in range(T):
    a = list(map(int, input().split()))
    summed.append(a[0]+a[1])
for i in range(T):
    print(f'Case #{i+1}:', summed[i])