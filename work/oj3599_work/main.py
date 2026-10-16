"""3599"""
a = int(input())
total = 0
while True:
    n = int(input())
    if n == -1:
        break
    total += n
    if total == a:
        break
print(total)
