"""3160"""
def main():
    """main"""
    a,b = [int(x) for x in input().split()]
    total = 0
    for i in range(a,b):
        if not i % 2:
            total += 1
    print(i)
    print(f"Total primes: {total}")
main()
