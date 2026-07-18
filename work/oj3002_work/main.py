"""Cyan's password generator"""
def main():
    """main"""
    name = input()
    uname = input()
    age = input()
    usename = name[:2] + uname[len(uname) - 1:] + age[len(age) - 1:]
    if len(name) >= 5 and len(uname) >= 5:
        print(usename)
    else:
        print(name[:1] + age + uname[len(uname) - 1:])
main()
