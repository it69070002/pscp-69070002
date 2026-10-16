"""3383"""
n = int(input())
m = int(input())
A = set()
B = set()
for _ in range(n):
    A.add(int(input()))
for _ in range(m):
    B.add(int(input()))
result = sorted(A - B)
print(*result)
