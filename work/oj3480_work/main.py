"""3480"""
N = int(input())
H = list(map(int, input().split()))
count = 0
for i in range(N):
    if i > 0 and H[i - 1] > H[i]:
        continue
    if i < N - 1 and H[i + 1] > H[i]:
        continue
    count += 1
print(count)
