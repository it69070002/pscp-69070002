"""3532"""
a = int(input())
b = int(input())
while b:
    r = a % b
    a = b
    b = r
print(abs(a))
