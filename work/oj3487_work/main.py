"""3487"""
n = int(input())
poles = []
for _ in range(n):
    poles.append(int(input()))
poles.sort()
total = 0
height = 0
for pole in poles:
    height += pole
    total += height * 2
print(total)
