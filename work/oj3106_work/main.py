"""3106"""
def main():
    """main"""
    number = int(input())
    c1000 = number // 1000
    c500 = (number - (1000*c1000)) // 500
    c100 = (number - (1000*c1000) - (500*c500)) // 100
    if 100 <= number <= 20000 and not number % 100:
        if c1000 > 0:
            print(f"1000 = {c1000}")
        if c500 > 0:
            print(f"500 = {c500}")
        if c100 > 0:
            print(f"100 = {c100}")
    else:
        print("ERROR")
main()
