"""3232"""
def main():
    """main"""
    a,b = map(int,input().split())
    total = 0
    for i in range(a,0,-2):
        total += i
        if total >= b:
            print((a - i) // 2 + 1)
            break
    else:
        print(-1)
main()
