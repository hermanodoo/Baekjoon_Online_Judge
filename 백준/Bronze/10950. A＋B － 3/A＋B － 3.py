T = int(input())
result = ''
for _ in range(T):
    a, b = map(int, input().split())
    result += (str(a + b) + '\n')
print(result)