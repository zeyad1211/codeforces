left, right = input().split("|")
# print(left, right)
weights = input()
leftlen = len(left)
rightlen = len(right)
lenword = len(weights)
i = 0
while(lenword > 0):
    if leftlen > rightlen:
        rightlen += 1
        right += weights[i]
        lenword -= 1
        i += 1
    elif(rightlen > leftlen):
        leftlen += 1
        left += weights[i]
        lenword -= 1
        i += 1
    else:
        rightlen += 1
        right += weights[i]
        lenword -= 1
        i += 1
if leftlen == rightlen:
    print(left + "|" + right)
else:
    print("Impossible")