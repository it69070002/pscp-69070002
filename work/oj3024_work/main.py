"""3024"""
def main():
    """main"""
    sum_a = float(input())
    max_a = float(input())
    min_a = sum_a - (max_a * 2)
    if min_a < 0:
        min_a = 0
    if (max_a - min_a) > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
