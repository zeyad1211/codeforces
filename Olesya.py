n, t = map(int, input().split())
smallestNumber = 10**(n-1)
largestNumber = 10**(n)
ans = -1
for i in range(smallestNumber, largestNumber): #largest Number is not included
    if (i%t == 0):
        ans = i
        break
print(ans)