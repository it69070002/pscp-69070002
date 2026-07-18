"""Pro"""
def main():
    """main"""
    x = int(input())
    y = int(input())
    a = float(input())
    z = float(input())
    o = int((z // x) * (y *a)) + ((z % x) * a)
    print(f'{o:.0f}')
main()
