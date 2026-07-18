"""3035"""
def main():
    """main"""
    r,x,y = [int(x) for x in input().split()]
    number_a = (x**2)+(y**2)
    number_b = r**2
    if number_a < number_b:
        print("IN")
    elif number_a == number_b:
        print("ON")
    else:
        print("OUT")
main()
