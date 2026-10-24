"""3611"""
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = int(input())
price1 = a + (e - 1) * a * (100 - b) / 100
price2 = e * a
if price2 >= d:
    price2 = price2 * (100 - c) / 100
else:
    price2 = e * a
if price1 < price2:
    print(1)
    print(f"{price1:.2f}")
else:
    print(2)
    print(f"{price2:.2f}")
