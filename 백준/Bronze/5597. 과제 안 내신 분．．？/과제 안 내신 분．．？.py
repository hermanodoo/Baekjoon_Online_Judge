t = [i for i in range(1, 31)]
s = list()
for _ in range(28):
    a = int(input())
    s.append(a)
b = [i for i in t if i not in s]
for i in b:
    print(i)