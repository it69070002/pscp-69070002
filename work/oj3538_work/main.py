"""3538"""
s = input()
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
ans = ""
for ch in s:
    if d[ch] % 2 == 1:
        ans += ch
        d[ch] = 0
if not ans:
    print("fully paired")
else:
    print(ans)
