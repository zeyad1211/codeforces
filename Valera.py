n = int(input())
string = "YES"
lst = [""]*n
for i in range(n):
    lst[i] = input()
temp = 0
temp2 = n-1
for j in range(n-1):
    if lst[j][temp] != lst[j+1][temp+1]:
        string = "NO"
        break
    if lst[-j][temp2] != lst[-j-1][temp2-1]:
        string = "NO"
        break
    temp += 1
    print(temp)
# print(lst[0][0])
print(lst)