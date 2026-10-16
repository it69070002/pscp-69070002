"""3395"""
_, _ = map(int, input().split())
H = [0] + list(map(int, input().split()))
A = list(map(int, input().split()))
max_height = 0
pos = 1
for target in A:
    while pos < target:
        max_height = max(max_height, H[pos])
        pos += 1
    answer = max(0, max_height - H[target] + 1)
    print(answer)
