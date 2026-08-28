"""main"""
def main():
    """main"""
    a =int(input())
    b =int(input())
    c =int(input())
    k = (a**2 + b**2) ** 0.5
    kk = (b**2 - c**2) ** 0.5
    kkk = (a**2 - c**2) ** 0.5
    if (a+b) > c and (a+c) > b and (b+c) > a:
        if a == b == c:
            print("EQUILATERAL")
        elif k == c or kk == a or kkk == b:
            print("RIGHT TRIANGLE")
        elif a == b or a == c or b == c:
            print("ISOSCELES")
        else:
            print("SCALENE")
    else:
        print("NOT A TRIANGLE")
main()
