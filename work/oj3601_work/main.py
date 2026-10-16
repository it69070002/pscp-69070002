"""3601"""
odd = 0
even = 0
while True:
    a = int(input())
    if a < 0:
        break
    if not a % 2:
        even += 1
    else:
        odd += 1
TOTAL = odd + even
print(odd, even, TOTAL)
