a = int(input())
num = 1
accu = 0
while accu < a:
    accu += num
    num += 1
if num % 2 == 0:
    print(accu - a+1,'/',num-accu+a-1, sep = "")
else:
    print(num-accu+a-1,'/',accu - a+1, sep = "")
    