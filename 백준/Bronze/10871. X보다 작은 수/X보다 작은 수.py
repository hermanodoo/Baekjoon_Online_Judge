N, X = map(int, input().split())
S = list(map(int, input().split()))
print(*[i for i in S if i < X])