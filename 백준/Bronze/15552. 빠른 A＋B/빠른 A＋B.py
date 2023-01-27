import sys
n = int(input())
for _ in range(n):
    print(sum(map(int, sys.stdin.readline().rstrip().split())))