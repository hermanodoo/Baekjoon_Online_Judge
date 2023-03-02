n = input()
if len(n) == 1:
    n = '0' + n
original = n
counter = 0

def cycle(n, original, counter):
    n = n[-1] + str(int(n[0]) + int(n[1]))[-1]
    counter += 1
    if n != original:
        cycle(n, original, counter)
    else:
        print(counter)

cycle(n, original, counter)
