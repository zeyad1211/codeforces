def isX():
    n = int(input())
    string = "YES"
    lst = [""]*(n)
    for i in range(0,n):
        lst[i] = input()
    temp = 0
    temp2 = n-1
    for j in range(0, n):
        for k in range(0, round((n/2))):
            if (lst[j][k] == lst[j][-k-1] and lst[j][k] == lst[-j-1][k]):
                string = "YES"
                if j == k or j+k == n-1:
                    if lst[j][k] != lst[0][0]:
                        string = "NO"
                        print(1)
                        return string
                else:
                    if lst[j][k] != lst[0][1]:
                        string = "NO"
                        print(2)
                        return string
            else:
                string = "NO"
                print(3)
                return string
                
        # print(lst)
    print(string)
answer = isX()
print(answer)