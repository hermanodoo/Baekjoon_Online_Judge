a = int(input())
b = 0

while 1:
    if a % 5 == 0:
        b += a // 5
        print(b)
        break
    else:
        a -= 3
        b += 1
    if a < 0:
        print(-1)
        break