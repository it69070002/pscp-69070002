"""3004"""
import math
def main():
    """main"""
    a,b,c = [int(x) for x in input().split()]
    d,e,f = [int(x) for x in input().split()]
    cal_d=math.sqrt((a-d)**2 + (b-e)**2 + (c-f)**2)
    print(f"{cal_d:.2f}")
main()
