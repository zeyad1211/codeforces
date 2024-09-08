n = int(input())
string = "YES"
lst = [""]*(n)
for i in range(0,n):
    lst[i] = input()
temp = 0
temp2 = n-1
for j in range(0, n):
    for k in range(0, round((n)/2)):
        if (lst[j][k] != lst[j][-k-1]):
            string = "NO"
            # print(f"{lst[j][k]}, {lst[j][-k-1]}")
            # print(f"{j}, {k}")
            break
# print(lst)
print(string)