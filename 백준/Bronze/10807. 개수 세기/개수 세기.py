import sys

n = input()
l = list(map(int, sys.stdin.readline().rstrip().split()))
print(l.count(int(input())))