notSelf = set()
all = [i for i in range(1, 10001)]
for i in range(1, 10001):
    t = i + sum([int(x) for x in str(i)])
    if t <= 10000:
        notSelf.add(t)
selfN = [i for i in all if i not in notSelf]
for i in selfN:
    print(i)
