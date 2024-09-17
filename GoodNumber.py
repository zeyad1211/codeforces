n, k = map(int,input().split())
tot = 0
dictionary = {}
for u in range(k+1):
    dictionary[str(u)] = 0
# print(dictionary)
for i in range(n):
    num = input()
    for j in range(k+1):
        if str(j) in num:
            dictionary[str(j)] += 1
    # print(dictionary)
    if 0 in dictionary.values():
        tot += 0
    else:
        tot += 1
print(tot)