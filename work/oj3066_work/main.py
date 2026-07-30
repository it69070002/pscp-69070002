"""3066"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    if a == b == c:
        print("all the same")
    elif a == b != c or a == c != b or b == c != a:
        print("neither")
    elif a != b != c:
        print("all different")
main()
