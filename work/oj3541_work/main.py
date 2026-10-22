"""3541"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if not b or not d:
    print(a * d)
else:
    exchange = (d - 1) // b
    total = (d - exchange) * a + exchange * c
    print(total)
