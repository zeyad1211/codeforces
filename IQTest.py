
def run():
    lst = [""]*4
    start1, start2, hashcount, dotcount = 0
    stop1, stop2 = 2
    for p in range(4):
        lst[p] = input()
    print(lst)
    while(stop1 < 5):
        for row in range(start1, stop1):
            for col in range(start2, stop2):
                if lst[row][col] == '#':
                    hashcount += 1
                else:
                    dotcount += 1
        if hashcount == 3 or dotcount == 3:
            return "YES"
        start2, stop2 += 1
        if stop2 == 4:
            start2 = 0
            stop2 = 2
            start1, stop1 += 1
    return "NO"
ans = run()
print(ans)