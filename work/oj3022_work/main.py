"""3022"""
def main():
    """main"""
    a = float(input())
    b = input().upper()
    can = input().upper()
    if b == "C":
        c = a
    elif b == "F":
        c = (a - 32) * 5 / 9
    elif b == "K":
        c = a - 273.15
    elif b == "R":
        c = a * 5 / 9 - 273.15
    else:
        return
    if can == "C":
        ans = c
    elif can == "F":
        ans = c * 9 / 5 + 32
    elif can == "K":
        ans = c + 273.15
    elif can == "R":
        ans = (c + 273.15) * 9 / 5
    else:
        return
    print(f"{ans:.2f}")
main()
