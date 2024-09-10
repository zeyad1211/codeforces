def isNextPrime():
    n, m = map(int, input().split())
    string = "YES"
    count = 0
    for k in range(2, m):
        if m%k == 0:
            string = "NO"
            return string
    for i in range(n+1,m):
        for j in range(2, i):
            if i%j == 0:
                count = 0
                break
            else:
                count += 1
        if count != 0:
            string = "NO"
            return string       
    return string

string = isNextPrime()
print(string)