def run():
    l, r = map(int, input().split())
    if r - l <= 1:
        print(-1)
        return
    if l % 2 != 0:
        l += 1
    if r % 2 != 0:
        r -= 1
    if r - l <= 1:
        print(-1)
        return
    print(l, l+1, l+2) 
    return
run()