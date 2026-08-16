"""3162"""
def main():
    """main"""
    number = int(input())
    x = 0
    for x in range(12):
        x += 1
        i = number * x
        print(f"{number} * {x} = {i}")
main()
