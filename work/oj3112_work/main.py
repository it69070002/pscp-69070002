"""3112"""
def main():
    """main"""
    a,b, = input().upper().split()
    extra = input().upper().split()
    price = 0
    if a == "S" and b == "R":
        price = 60
    elif a == "M" and b == "R":
        price = 80
    elif a == "L" and b == "R":
        price = 100
    elif a == "S" and b == "T":
        price = 80
    elif a == "M" and b == "T":
        price = 100
    elif a == "L" and b == "T":
        price = 120
    if extra[0] == "P":
        price += 15 * int(extra[1])
    elif extra[0] == "E":
        price += 10 * int(extra[1])
    print(price)
main()
    