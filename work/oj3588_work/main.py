"""3588"""
import math
a = int(input())
n = 0
for _ in range(a):
    m = int(input())
    n = math.gcd(n,m)
print(n)
