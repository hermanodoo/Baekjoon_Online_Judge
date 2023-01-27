import sys
a, b = 1, 1
while 1:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)