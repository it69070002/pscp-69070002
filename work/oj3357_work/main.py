"""3357"""
n = int(input())
h = []
for i in range(n):
    h.append(int(input()))
count = 0
for i in range(n):
    left = (not i or h[i] > h[i - 1])
    right = (i == n - 1 or h[i] > h[i + 1])
    if left and right:
        count += 1
print(count)
