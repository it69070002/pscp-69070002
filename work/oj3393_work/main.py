"""3393"""
n = int(input())
a = list(map(int, input().split()))
s = input()
pos = a.index(1)
treasure = a.index(2)
for c in s:
    if c == 'R':
        new_pos = pos + 1
    else:
        new_pos = pos - 1
    if new_pos < 0 or new_pos >= n:
        continue
    pos = new_pos
    if pos == treasure:
        break
a[a.index(1)] = 0
a[pos] = 1
print(*a)
