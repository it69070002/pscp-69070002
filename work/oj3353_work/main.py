"""3353"""
a = list(map(int, input().split()))
b = False
for i in reversed(a):
    if not i % 3 or not i % 5:
        print(i)
        b = True
if not b:
    print("Nope")
