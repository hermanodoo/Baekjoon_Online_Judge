t = int(input())
for _ in range(t):
    room_1 = 1
    floor = int(input()) - 1
    room = int(input())
    residents = [i for i in range(1, room+1)]
    for _ in range(floor+1):
        for i in range(1, room):
            residents[i] = (residents[i-1] + residents[i])
    print(residents[-1])