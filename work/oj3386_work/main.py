"""3386"""
m = int(input())
n = int(input())
a = [input() for i in range(m)]
b = [input() for i in range(n)]
c = sorted(set(a) & set(b), reverse=True)
if c:
    for x in c:
        print(x)
else:
    print("Nope")
