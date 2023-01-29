n = int(input())
for _ in range(n):
    s = list(map(int, input().split()))
    score = s[1:]
    avg = sum(score)/len(score)
    over = [i for i in score if i > avg]
    print('%.3f'% (len(over)/s[0]*100), '%', sep="")