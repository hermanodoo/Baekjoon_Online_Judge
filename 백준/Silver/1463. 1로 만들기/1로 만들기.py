n = int(input())

ls = [0] * (n+1)

for i in range(2, n + 1):
    ls[i] = ls[i-1] + 1
    if i % 2 ==0:
        ls[i] = min(ls[i], ls[i//2] + 1)
    if i % 3 ==0:
        ls[i] = min(ls[i], ls[i//3] + 1)
                
print(ls[n])



