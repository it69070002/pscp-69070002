"""3068"""
def main():
    """main"""
    year = int(input())
    if not year < 1852:
        print("yes")
    else:
        print("no")
    if not year % 4:
        if not year % 100:
            if not year % 400:
                print("yes")
            else:
                print("no")
        else:
            print("yes")
    else:
        print("no")
main()
