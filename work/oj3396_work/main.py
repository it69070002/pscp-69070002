"""3396"""
N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]
fastest = min(S)
count = 0
for s in S:
    if K * fastest > (K - 1) * s:
        count += 1
print(count)
