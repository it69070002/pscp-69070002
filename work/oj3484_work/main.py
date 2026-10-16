"""3484"""

N, P = input().split()
N = int(N)
P = float(P)

a = []
for i in range(N):
    row = list(map(int, input().split()))
    a.append(row)

row_tile = [0] * N
row_point = [0] * N
col_tile = [0] * N
col_point = [0] * N

total_tile = 0
total_point = 0

for i in range(N):
    for j in range(N):
        if a[i][j] > 0:
            row_tile[i] += 1
            col_tile[j] += 1
            total_tile += 1

        row_point[i] += a[i][j]
        col_point[j] += a[i][j]
        total_point += a[i][j]

for i in range(N):
    print(*a[i], row_tile[i], row_point[i])

print(*col_tile)
print(*col_point)
print(total_tile, total_point, format(total_point * P, ".2f"))
