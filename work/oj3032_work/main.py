"""3032"""
def main():
    """main"""
    top = int(input())
    a = []
    for x in range(0,top):
        a.append(int(input()))
    x = max(a)
    print(x)
    print(a.count(x))
main()
