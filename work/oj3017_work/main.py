"""3017"""
def main():
    """main"""
    money = float(input())
    money_a = money * 0.10
    if  money_a < 50:
        money_a = 50
    elif money_a > 1000:
        money_a = 1000
    total = money + money_a
    total += total * 0.07
    print(f"{total:.2f}")
main()
