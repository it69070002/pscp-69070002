"""3292"""
k = input()
n = int(input())
for x in k:
    if x == "R":
        for i in range(n):
            print(" " * (2 * i) + "*" * (n - i))
        for i in range(n - 2, -1, -1):
            print(" " * (2 * i) + "*" * (n - i))
        print()
    elif x == "L":
        for i in range(n):
            print(" " * (n - 1 - i) + "*" * (n - i))
        for i in range(n - 2, -1, -1):
            print(" " * (n - 1 - i) + "*" * (n - i))
        print()
