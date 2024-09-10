n = int(input())
ans = 1
for i in range(n):
    ans *= 8
    ans %= 10
print(ans)