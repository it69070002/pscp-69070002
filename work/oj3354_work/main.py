"""3354"""
def check(num, op, x):
    """ตรวจสอบเงื่อนไขของตัวเลข"""
    if op == "==":
        return num == x
    if op == ">":
        return num > x
    if op == "<":
        return num < x
    if op == ">=":
        return num >= x
    if op == "<=":
        return num <= x
    if op == "!=":
        return num != x
    return False
a, o = input().split()
b, y = input().split()
c, z = input().split()
o = int(o)
y = int(y)
z = int(z)
for i in range(1000):
    h = i // 100
    t = (i // 10) % 10
    u = i % 10

    if check(u, a, o) and check(t, b, y) and check(h, c, z):
        print(f"{i:03d}")
