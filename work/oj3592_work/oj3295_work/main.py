"""3295"""
n = int(input())
if n <= 10:
    cost = n * 5
elif n <= 50:
    cost = 50 + (n - 10) * 7
elif n <= 100:
    cost = 330 + (n - 50) * 10
elif n <= 200:
    cost = 830 + (n - 100) * 12
else:
    cost = 2030 + (n - 200) * 15
total = cost * 107 + n * 50
total = (total + 5) // 10
print(f"{total // 10}.{total % 10}")
