word = input()

length = len(word)
lower = ""
upper = ""

if length % 2 == 0:
    lower = word[:length // 2]
    upper = word[length:length // 2-1:-1]
else:
    lower = word[:length // 2 + 1]
    upper = word[length:length // 2 - 1:-1]

print(1 if lower == upper or length == 1 else 0)
