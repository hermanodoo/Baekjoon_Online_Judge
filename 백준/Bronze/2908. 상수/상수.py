a, b = input().split()

def reverse(n):
    n = list(reversed([i for i in n]))
    f = int(''.join(n))
    return f
    
print(max(reverse(a), reverse(b)))