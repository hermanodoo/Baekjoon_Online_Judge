t = int(input())

c = 0
for _ in range(t):
    rep = ""
    rep_list = list()
    word = input()
    for i in range(len(word)):
        if word[i] == rep:
            continue
        else:
            rep = word[i]
            rep_list.append(word[i])

    rep_set = set(rep_list)
    if len(rep_set) == len(rep_list):
        c += 1

print(c)