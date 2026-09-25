"""3301"""
w,l,m,n = map(int,input().split())
ans = w * l
for a in range(m,n + 1):
    x = l // a
    r = l % a
    used = w * a * x + a * r * (w // a)
    ans = min(ans, w * l - used)
print(ans)
