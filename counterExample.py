def run():
    l, r = map(int, input().split())
    cf =  []
    for i in range(2, l+1):
        if l % i == 0 and r % i == 0:
            commonFactor = i
            b = l + commonFactor - 1
            if b < r:
                print(l, b, r)
                return
            else:
                print(-1)
                return
        if l%i == 0:
            cf.append(i)
    c = l*cf[0]
    if c < r:
        print(l, l+1,l*cf[0])
    else:
        print(-1)
    return
run()