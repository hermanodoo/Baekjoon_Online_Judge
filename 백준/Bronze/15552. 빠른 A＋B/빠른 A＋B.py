import sys
T = int(input())

for _ in range(T):
  data = list(map(int,sys.stdin.readline().rstrip().split()))
  print(data[0]+data[1])