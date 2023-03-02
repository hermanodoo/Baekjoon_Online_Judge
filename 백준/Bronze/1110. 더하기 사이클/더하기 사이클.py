n = int(input())
original = n
counter = 0

def cycle(n, original, counter):
    n = (n * 10 + n if n < 10 else (n % 10)*10 + (n // 10 + n % 10) % 10)
    counter += 1
    if n != original:
        cycle(n, original, counter)
    else:
        print(counter)

cycle(n, original, counter)
