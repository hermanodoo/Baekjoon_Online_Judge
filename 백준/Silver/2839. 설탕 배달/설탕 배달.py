weight = int(input())
counter = 0

while 1:
    if weight % 5 == 0:
        counter += weight // 5
        print(counter)
        break
    else:
        weight -= 3
        counter += 1
    if weight < 0:
        print(-1)
        break