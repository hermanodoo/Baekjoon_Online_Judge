import sys

while 1:
    data = list(map(int,sys.stdin.readline().rstrip().split()))
    if data[0] == 0 & data[1] == 0:
        break
    print(data[0]+data[1])