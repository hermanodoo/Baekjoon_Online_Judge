import sys
from statistics import mean

T = int(input())
for _ in range(T):
    s = list(map(int, sys.stdin.readline().split()))
    sc = s[1:]
    m = mean(sc)
    over = [i for i in sc if i > m]
    per = float(len(over)/len(sc)*100)
    print('%.3f'%per, '%', sep ='')
    