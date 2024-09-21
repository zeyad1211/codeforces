n = int(input())
directions = input()
positions = list(map(int, input().split()))
collision = False
distances = []
start = 0
ans = 0
diff = 0
# print(absolute)
while(ans != -1):
    ans = directions.find("RL", start)
    if ans != -1:
        diff = int((positions[ans+1] - positions[ans])/2)
        distances.append(diff)
        start = ans+2
if len(distances) > 0:
    print(min(distances))
else:
    print(-1)