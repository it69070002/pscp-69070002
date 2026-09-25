"""3300"""
n = int(input())
total = 0
for _ in range(n):
    h = int(input())
    if h > 18:
        total += 1
answer = max(n, 2 * total - 1)
print(answer)
