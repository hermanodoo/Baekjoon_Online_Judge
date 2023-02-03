s = input().upper()
t = list(set(s))
ct = list()
for i in t:
    a = s.count(i)
    ct.append(a)
ct = [int(i) for i in ct]
if ct.count(max(ct)) == 1:
    print(t[ct.index(max(ct))])
else:
    print('?')