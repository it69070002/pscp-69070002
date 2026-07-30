"""3067"""
def main():
    """main"""
    a = float(input())
    b = float(input())
    c = float(input())
    if a > b > c:
        print("decreasing")
    elif a < b < c:
        print("increasing")
    else:
        print("neither")
main()
