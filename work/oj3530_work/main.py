"""3530"""
n = int(input())
count = 0
for a in range(1, n + 1):
    free = True
    for b in range(2, int(a ** 0.5) + 1):
        if not a % (b * b):
            free = False
            break
    if free:
        count += 1
print(count)
