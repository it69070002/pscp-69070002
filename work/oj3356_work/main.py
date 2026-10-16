"""3356"""
n = int(input())
m = int(input())
k = int(input())
for i in range(n - 1, -1, -1):
    for j in range(m):
        num = j * n + i + 1
        if num == k:
            print("XX", end=" " if j < m - 1 else "")
        else:
            print(f"{num:02d}", end=" " if j < m - 1 else "")
    print()
    if not i % 2 and i:
        print()
