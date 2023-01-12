T = int(input())

re = list()

for i in range(T):
    a = list(map(int, input().split()))
    re.append(f'Case #{i+1}: {a[0]} + {a[1]} = {a[0]+a[1]}')
for i in re:
    print(i)