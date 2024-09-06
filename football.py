n = int(input())
diction = {}
for i in range(n):
    inpt = input()
    if inpt not in diction:
        diction[inpt] = 0
    diction[inpt] +=1

val = max(diction.values())
for key, value in diction.items():
    if value == val:
        print(key)
        break