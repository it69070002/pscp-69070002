"""3644"""
import json
a = json.loads(input())
n = int(input())
s = int(input())
maximum = 0
for i in range(256):
    total = 0
    pos = i
    for j in range(n):
        total += a[pos]
        pos = (pos + s) % 256
    if total > maximum:
        maximum = total
print(maximum)
