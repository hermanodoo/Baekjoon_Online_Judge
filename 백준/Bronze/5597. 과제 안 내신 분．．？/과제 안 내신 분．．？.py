a = list()
full = [i for i in range(1, 31)]
for _ in range(28):
    a.append(int(input()))
nohw = [i for i in full if i not in a]
nohw.sort()
print(nohw[0], nohw[1], sep ='\n')