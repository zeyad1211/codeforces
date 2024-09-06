n, m = map(int, input().split())
lst = []
color = 0
for i in range(n):
    lst.append(list(input().split()))
for arr in lst:
    if ('C' in arr or 'M' in arr or 'Y' in arr):
        color = 1
        break
if (color == 1):
    print("#Color")
else:
    print("Black&White")