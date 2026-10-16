"""3385"""
p = int(input())
n = int(input())
stops = {}
for _ in range(n):
    data = list(map(int, input().split()))
    stops[data[0]] = data[1:]
bus = []
ans = 0
for stop in range(1, n + 1):
    next_bus = []
    for dest in bus:
        if dest == stop:
            ans += 1
        else:
            next_bus.append(dest)
    bus = next_bus
    for dest in stops.get(stop, []):
        if dest > stop and len(bus) < p:
            bus.append(dest)
print(ans)
