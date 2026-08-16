"""3113"""
def main():
    """main"""
    s, t = input().split()

    if s == 'S' and t == 'R':
        price = 60
    elif s == 'S' and t == 'T':
        price = 80
    elif s == 'M' and t == 'R':
        price = 80
    elif s == 'M' and t == 'T':
        price = 100
    elif s == 'L' and t == 'R':
        price = 100
    else:
        price = 120

    a = input().split()
    if a[0] == 'P':
        price += int(a[1]) * 15
    elif a[0] == 'E':
        price += int(a[1]) * 10
    print(price)
main()
