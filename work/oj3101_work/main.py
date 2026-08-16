"""3101"""
def main():
    """main"""
    heat = int(input())
    heat_a = input().lower()
    if heat_a == "c":
        if heat <= 0:
            print("solid")
        elif heat >= 100:
            print("gas")
        else:
            print("liquid")

    elif heat_a == "f":
        if heat <= 32:
            print("solid")
        elif heat >= 212:
            print("gas")
        else:
            print("liquid")
main()
