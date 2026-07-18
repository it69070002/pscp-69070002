"""2992"""
def main():
    """main"""
    a = input()
    b = input()
    ab = int(a[-1] + a[0])
    if b == "+":
        print(f'{a} + {ab} = {int(a)+ab}')
    else:
        print(f'{a} * {ab} = {int(a)*ab}')
main()
