"""3022"""
def main():
    """main"""
    a = float(input())
    b = input()
    can = input()
    k = a + 273.15
    f = a * 9 / 5 + 32
    r = (a + 273.15) * 9 / 5
    add = (b==a)
    o = int(can)
    if add == (k):
        print(o)
    elif add == (f):
        print(o)
    elif add == (r):
        print(o)
    print(f"{o:.2f}")
main()
