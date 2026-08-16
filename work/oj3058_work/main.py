"""3058"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    goal = int(input())
    big = min(b, goal // 5)
    r = goal - big * 5
    if r <= a:
        print(r)
    else:
        print(-1)
main()
