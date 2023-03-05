import sys
t = int(sys.stdin.readline().rstrip())
a, b = 0, 0
for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(a+b)+'\n')
