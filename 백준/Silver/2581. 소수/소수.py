M = int(input())
N = int(input())
yes = set()

for i in range(M, N+1):
    check = list()
    a = 2
    while i != 1:
        if i % a == 0:
            check.append(a)
            i = int(i / a)
        else:
            a += 1
    if len(check) == 1:
        yes.add(*check)

if len(yes) == 0:
    print(-1)
else:
    print(sum(yes), min(yes))