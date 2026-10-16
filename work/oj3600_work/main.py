"""3600"""
total = 0
while True:
    order = int(input())
    if order == 5:
        print("Bye Bye")
        break
    if order == 1:
        total += 100
    elif order == 2:
        total += 120
    elif order == 3:
        total += 200
    elif order == 4:
        total += 60
print(f"Total Calories: {total}")
