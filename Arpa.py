n = int(input())
if n == 0:
    print(1)
elif n in range(1, 10**9+1, 4):
    print(8)
elif n in range(2, 10**9+1, 4):
    print(4)
elif n in range(3, 10**9+1, 4):
    print(2)
else:
    print(6)