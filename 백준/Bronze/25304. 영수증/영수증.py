tot = int(input())
I = int(input())
summ = 0
for _ in range(I):
    p, n = map(int, input().split())
    summ += p*n
    
if summ == tot:
    print('Yes')
else:
    print('No')