from statistics import mean 

N = int(input())
tot = 0
score = list(map(int, input().split()))
m = max(score)
a = mean(score)
print(a/m*100)