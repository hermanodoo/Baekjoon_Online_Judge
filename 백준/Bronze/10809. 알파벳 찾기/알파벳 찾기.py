S = input()
l = list()
for i in range(ord('a'), ord('z')+1):
    t = S.find(chr(i))
    l.append(t)
print(*l)