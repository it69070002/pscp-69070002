"""3236"""
def main():
    """main"""
    n = int(input())
    a = input()
    b = input()
    count = 0
    for i in range(n):
        if int(a[i]) + int(b[i]) != 9:
            count += 1

    if not count:
        print("YES")
    else:
        print("NO", count)
main()
