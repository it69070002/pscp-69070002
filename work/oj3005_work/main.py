"""กระต่ายน้อยจ่ายตลาด"""
def main():
    """main"""
    a,b,c = [int(x) for x in input().split()]
    r1 = 10*a
    r2 = 25*b
    r3 = 3*c
    s = r1+r2+r3
    print(s)
main()
