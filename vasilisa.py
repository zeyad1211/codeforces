def run():
    r1, r2 = map(int, input().split())
    c1, c2 = map(int, input().split())
    d1, d2 = map(int, input().split())

    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                for k in range(1, 10):
                    if len({x,y,z,k}) < 4:
                        continue
                    if r1 == x+y and r2 == z+k and c1 == x+z and c2 ==y+k and d1 == x+k and d2 == y+z:
                        print(x,y)
                        print(z, k)
                        return
    print(-1)
    return
run()