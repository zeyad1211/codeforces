n = int(input())
total = 0
for i in range(n):
    shape = input()
    if shape[0] == "T":
        num = 4
    elif shape[0] == "C":
        num = 6
    elif shape[0] == "O":
        num = 8
    elif shape[0] == "D":
        num = 12
    elif shape[0] == "I":
        num = 20
    total += num
print(total)