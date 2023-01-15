s = input()
s = [i for i in s]
ct = 0
alp = [chr(i) for i in range(65, 65+26)]
for i in s:
    ind = alp.index(i)
    if 15 <= ind <= 18 or 22 <= ind <= 25:
        if 15 <= ind <= 18:
            dial = 8
        else:
            dial = 10
    elif 19 <= ind <= 21:
        dial = 9
    else:
        dial = ind // 3 + 3
    ct += dial
print(ct)