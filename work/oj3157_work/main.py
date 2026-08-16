"""3157"""
def main():
    """main"""
    point = int(input())
    total = 0
    for _ in range(point):
        n = input()
        if n == "+":
            total += 10
        elif n == "-":
            total -= 5
    print(total)
main()
