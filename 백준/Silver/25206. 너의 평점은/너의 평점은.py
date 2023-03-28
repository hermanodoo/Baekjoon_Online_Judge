import sys

grades = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0, 'P': 0}

total = 0
info = ''
denominator = 0

for _ in range(20):
    info = sys.stdin.readline().strip().split()
    if info[2] != 'P':
        total += (float(info[1]) * grades[info[2]])
        denominator += float(info[1])
sys.stdout.write(str(total / denominator))
