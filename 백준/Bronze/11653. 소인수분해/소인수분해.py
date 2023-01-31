n = int(input())
li = list()
i = 2
while n != 1:
    if n % i == 0:
        li.append(i)
        n = int(n / i)
    else:
        i += 1
print(*li, sep='\n')