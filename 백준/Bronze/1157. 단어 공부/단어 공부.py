s = input().upper()
t = list(set(s))
maxx = 0
ch = 0
ct = list()

for i in t:
    a = s.count(i)
    ct.append(a)
ct = [int(i) for i in ct]

if ct.count(max(ct)) == 1:
    print(t[ct.index(max(ct))])
#elif ct.count(max(ct)) != 1:
#    print('?')
else:
    print('?')