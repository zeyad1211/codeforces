n, k = map(int,input().split())
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
tot = min(dictionary.values())
print(tot)