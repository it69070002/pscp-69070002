"""3163"""
def main():
    """main"""
    n = int(input())
    odd = 0
    even = 0
    total = 0
    for _ in range(n):
        number = int(input())
        total += number
        if not number % 2:
            even += 1
        else:
            odd += 1
    print(f"SUM {total}")
    print(f"EVEN {even}")
    print(f"ODD {odd}")
main()
