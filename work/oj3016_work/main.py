"""Seven"""
def main():
    """main"""
    number = int(input())
    b = str(7 ** (number % 4))
    print(b[-1])
main()
