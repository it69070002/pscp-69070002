"""3070"""
def main():
    """main"""
    odd = 0
    even = 0
    for _ in range(3):
        n = int(input())
        if not n % 2:
            even += 1
        else:
            odd += 1
    print(even)
    print(odd)
main()
