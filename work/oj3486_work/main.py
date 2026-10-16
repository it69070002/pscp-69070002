"""3486"""

n = int(input())
shots = []

for _ in range(n):
    x, y, d = map(int, input().split())
    shots.append((x, y, d * d))

for tx in range(1000):
    for ty in range(1000):
        valid = True

        for x, y, d2 in shots:
            if (tx - x) ** 2 + (ty - y) ** 2 != d2:
                valid = False
                break

        if valid:
            print(tx, ty)
            raise SystemExit
