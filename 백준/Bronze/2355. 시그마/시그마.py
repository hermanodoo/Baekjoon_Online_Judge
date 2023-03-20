import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
tot = (abs(a - b) + 1) / 2 * (a + b)
sys.stdout.write(str(int(tot)))
