n = int(input())
ans = 0
if n%2 == 0:
    ans = n/2
else:
    ans = -1*((n+1)//2)
print(int(ans))