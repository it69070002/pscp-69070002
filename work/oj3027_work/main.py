"""3027"""
def main():
    """main"""
    a,b,c = [int(x) for x in input().split()]
    s = int(input())
    ab =  ((a + b) * 2) * c
    bb = ab * s
    print(ab)
    print(bb)
main()
