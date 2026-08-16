"""3129"""
def main():
    """main"""
    name = int(input())
    n = []
    for _ in range(name):
        n.append(int(input()))
        x = sum(n)
        y = max(n)
        i = min(n)
        j = x / len(n)
    print(x)
    print(y)
    print(i)
    print(f"{j:.1f}")
main()
