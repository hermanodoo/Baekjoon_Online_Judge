N = int(input())
s = [" " for i in range(N)]
for i in range(1, N+1):
    s[-i] = '*'
    print(*s, sep = '')