"""3298"""
s = input()
t = s.lower()
a = t.split('b')
mx = 0
for x in a:
    u = len(x) - len(x.lstrip('u'))
    mx = max(mx, u)
if mx >= 2:
    print("Yes", mx)
elif 'b' in t:
    i = t.index('b')
    print((s[:i+1] + 'U' * (len(s)-i-1)).upper())
else:
    print(("BUU" * 3)[:len(s)])
    