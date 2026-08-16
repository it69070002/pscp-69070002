"""3071"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    d = int(input())
    r = int(input())
    sum_x = 0
    for i in range(a, b + 1):
        if i % d == r:
            sum_x += 1
    print(sum_x)
main()
