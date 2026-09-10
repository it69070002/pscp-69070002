"""3233"""
def main():
    """main"""
    text = input().split()
    ticket = input().split()
    letter = text[0] == ticket[0]
    number = text[1] == ticket[1]
    last2 = text[1][-2:] == ticket[1][-2:]
    last3 = text[1][-3:] == ticket[1][-3:]
    if letter and number:
        print(1000000)
    elif number:
        print(100000)
    elif letter and last3:
        print(2000)
    elif letter and last2:
        print(1000)
    elif last3:
        print(200)
    elif last2:
        print(100)
    elif letter:
        print(20)
    else:
        print(0)
main()
