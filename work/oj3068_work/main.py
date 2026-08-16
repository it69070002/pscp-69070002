"""3068"""
def main():
    """main"""
    year = int(input())
    if 1 <= year <= 2026:
        if not year % 4:
            print("yes")
        elif not year % 100:
            print("no")
        elif not year % 400:
            print("yes")
        else:
            print("no")
main()
