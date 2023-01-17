self_num = list()
for i in range(1, 10001):
    start = str(i)
    splitted = [int(i) for i in start] + [i]
    final = sum(splitted)
    self_num.append(final)
nothing = [i for i in range(1, 10001)]
no_self = [i for i in nothing if i not in self_num]
for i in no_self:
    print(i)