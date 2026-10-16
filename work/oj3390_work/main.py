"""3390"""
a = []
for i in range(5):
    a.append(list(map(int, input().split())))
row = -1
col = -1
for i in range(5):
    if sum(a[i]) % 2:
        row = i
for j in range(5):
    total = sum(a[i][j] for i in range(5))
    if total % 2:
        col = j
if row != -1 and col != -1:
    print(row, col)
else:
    print(-1, -1)
