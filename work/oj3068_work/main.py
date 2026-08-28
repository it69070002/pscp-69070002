"""3068"""
def main():
    """main"""
    year = int(input())
    if year < 1582:
        leap = not year % 4
    else:
        leap = not year % 400 or (not year % 4 and bool(year % 100))

    if leap:
        print("yes")
    else:
        print("no")
main()
