"""3358"""
n = int(input())
w = list(map(int, input().split()))
total = 0
result = []
for i in range(n):
    a = w[2*i]
    b = w[2*i+1]
    if a > b:
        big = a
    else:
        big = b
    total += big
    result.append(big)
if n == 1:
    print(total)
else:
    print(" + ".join(map(str, result)), "=", total)
