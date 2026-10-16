"""3387"""
t = tuple(input().split())
x = input()
pos = t.index(x)
n = t.count(x)
for _ in range(n):
    print(*([pos] * n))
