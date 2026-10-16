"""3394"""
N, S = map(int, input().split())
a = [int(input()) for _ in range(N)]
seen = set()
cur = S
while cur and cur not in seen:
    seen.add(cur)
    cur = a[cur - 1]
print(len(seen))
