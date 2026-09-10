"""3234"""
color, n = input().split()
n = int(n)
for _ in range(n):
    if color == "R":
        print("Red", end=" ")
        color = "G"
    elif color == "G":
        print("Green", end=" ")
        color = "B"
    else:
        print("Blue", end=" ")
        color = "R"
