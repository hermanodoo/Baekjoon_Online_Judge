a = input()
b = input()
b = [int(i) for i in b]

summa = 0

for i in range(len(a)):
    t = int(a)*b[-i - 1]
    summa += t*10**i
    print(t)
    
print(summa)
    