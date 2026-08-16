"""3105"""
def main():
    """main"""
    rate = int(input())
    total = 0
    if 0 < rate <= 1:
        total = 35
    elif 1 < rate <= 10:
        total = 35 + (rate - 1) * 5
    elif rate > 10:
        total = 35 + (9 * 5) + (rate - 10) * 8
    print(total)
main()
