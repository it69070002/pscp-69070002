"""3063"""
def main():
    """main"""
    text = input()
    number = int(input())
    if (text) == "H" and (number) == 4567:
        pwd = "safe unlocked"
    elif (text) == "H":
        pwd = "safe locked - change digit"
    elif (number) == 4567:
        pwd = "safe locked - change char"
    else:
        pwd = "safe locked"
    print(pwd)
main()
