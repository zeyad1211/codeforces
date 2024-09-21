def run():
    n = int(input())
    x = int(input())
    a, b = map(int, input().split())
    lst = [x, 7-x]
    # print(lst)
    for i in range(n-1):
        a, b = map(int, input().split())
        if a in lst or b in lst:
            return "NO"
    return "YES"

ans = run()
print(ans)
