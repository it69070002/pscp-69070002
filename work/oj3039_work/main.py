"""3039"""
def main():
    """main"""
    top = int(input())
    a = []
    for _ in range(0,top):
        a.append(int(input()))
        a.sort()
    print(a[0])
main()
