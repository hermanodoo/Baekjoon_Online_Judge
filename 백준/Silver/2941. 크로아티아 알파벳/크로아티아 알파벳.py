letters = input()

croatia = ('c=', 'c-', 'dz=', 'z=', 'd-', 'lj', 'nj', 's=')

c = 0
for i in croatia:
    for j in letters:
        if i in letters:
            letters = letters.replace(i, " ", 1)
            c += 1

letters = [i for i in ''.join(letters.split())]
print(c + len(letters))