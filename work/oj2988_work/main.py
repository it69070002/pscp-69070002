"""การตรวจสอบบัตรประชาชน"""
def main():
    """main"""
    number = input()
    if len(number) == 13:
        print("yes")
    else:
        print("no")
main()
