N = int(input())

for _ in range(N):
    score = 0
    accu = 0
    s = input()
    leng = len(s)
    for i in range(leng):
        if s[i] == 'O':
            score += 1
            accu += score
        else:
            score = 0
            accu += score
            continue
    print(accu)