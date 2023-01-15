n = int(input())
for _ in range(n):
    a, s = input().split()
    l = list()
    for i in range(len(s)):
        l.append(s[i]*int(a))
    print(*l, sep="")