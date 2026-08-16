"""3014"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    total = d // a
    if not b or not c:
        print(total)
    else:
        caps = total
        while caps >= b:
            ex = (caps // b) * c
            total += ex
            caps = (caps % b) + ex
        print(total)
main()
