"""3592"""
size = int(input())
a = input()
text = input()
if a == "left":
    print(text.ljust(size))
elif a == "right":
    print(text.rjust(size))
else:
    n = size - len(text)
    print(" " * ((n + 1) // 2) + text + " " * (n // 2))
