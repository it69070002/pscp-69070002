"""3481"""
L, N = map(int, input().split())
bridges = []
for _ in range(N):
    A, B = map(int, input().split())
    bridges.append((A, B))
ans = 0
for x in range(L + 1):
    cnt = 0
    for A, B in bridges:
        if A < x <= B:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
