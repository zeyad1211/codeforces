n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(input().split()))
if 'C' or 'M' or 'Y' in lst:
    print("#Color")
else:
    print("#Black&White")