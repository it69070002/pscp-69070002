"""3231"""
def main():
    """main"""
    g = int(input())
    r = int(input())
    if g not in range(1, 7) or r not in range(1, 7):
        print("Invalid")
    elif g == r:
        print("Correct!")
    else:
        print("Wrong!")
main()
