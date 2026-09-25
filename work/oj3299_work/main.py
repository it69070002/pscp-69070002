"""3299"""
L, N = map(int, input().split())
total = 0
for i in range(1, N + 1):
    total += i
    if total >= N:
        break
s = (i + L - 1) // L
print(s)
