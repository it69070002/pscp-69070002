"""3021"""
import math
def main():
    """main"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())
    distance = math.sqrt((a - d) ** 2 + (b - e) ** 2)
    if distance <= c + f:
        print("overlapping")
    else:
        print("no overlapping")
main()
