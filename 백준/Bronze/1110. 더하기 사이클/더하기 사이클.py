n = int(input())
m = n
o = -1
t = 0

while 1:
    if o != m:
        if n < 10:
            n = n*10 + n
            o = n
            t += 1
        else:
            n = (n%10)*10 + (n//10 + n%10)%10
            o = n
            t += 1
    else:
        print(t)
        break