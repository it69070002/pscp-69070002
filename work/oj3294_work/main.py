"""3294"""
def main():
    """main"""
    n = int(input())
    a = int(input())
    total = n * a
    if not total:
        print("No teaching")
    elif total < 60:
        print(f"{total} minute")
    else:
        hours = total // 60
        minute = total - hours * 60
        if not minute:
            print(f"{hours} hours")
        else:
            print(f"{hours} hours {minute} minute")
main()
