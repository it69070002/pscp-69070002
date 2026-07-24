"""3062"""
def main():
    """main"""
    age = int(input())
    message = input()
    if age <= 17 or message in ('s', 'S'):
        print(20)
    else:
        print(50)
main()
