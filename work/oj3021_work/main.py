"""3010"""
import math
def main():
    """3010"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())
    math_a = math.sqrt((a-d)**2 + (b-e)**2)
    math_b = math_a * (c + f)
    if math_b:
        print("overlapping")
    else:
        print("no overlapping")
main()
