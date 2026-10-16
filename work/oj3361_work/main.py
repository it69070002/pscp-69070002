"""3361"""
n = int(input())
cars = []
for i in range(n):
    _, v = map(int, input().split())
    cars.append(v)
max_v = 0
count = 0
for i in range(n - 1, -1, -1):
    if cars[i] < max_v:
        count += 1
    else:
        max_v = cars[i]
print(count)
