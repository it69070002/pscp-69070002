"""การตรวจสอบบัตรนักศึกษา"""
def main():
    """main"""
    number = input()
    if number[2:3] == '1' and number[3:4] == '6':
        print("yes")
    else:
        print("no")
main()
