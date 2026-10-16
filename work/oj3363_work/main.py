"""3363"""
R, C = map(int, input().split())
x, y = map(int, input().split())
N = int(input())
a = [[0] * C for _ in range(R)]
for _ in range(N):
    r, c = map(int, input().split())
    for i in range(R):
        for j in range(C):
            if abs(i - r) <= 2 and abs(j - c) <= 2:
                if i == r and j == c:
                    a[i][j] = 100
                elif abs(i - r) <= 1 and abs(j - c) <= 1:
                    a[i][j] = max(a[i][j], 60)
                else:
                    a[i][j] = max(a[i][j], 20)
safe = 0
for i in range(R):
    for j in range(C):
        if not a[i][j]:
            safe += 1
print(safe)
print(str(a[x][y]) + "%")
