"""3542"""
n = int(input())
total = 0
i = 1
while i <= n:
    j = min(n, i * 10 - 1)
    total += (j - i + 1) * len(str(i))
    i *= 10
total += n - 1
if n > 1:
    total += 1
print(total)
