import math
n, m, a = map(int, input().split())
maxi = max(n, m)
if n > a and m > a:
    rows = math.ceil(n/a)
    cols = math.ceil(m/a)
    ans = rows * cols
elif maxi > a:
    ans = math.ceil(maxi/a)
else:
    ans = 1
print(ans)
