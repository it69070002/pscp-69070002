"""3017"""
def main():
    """main"""
    money = int(input())
    money_a = money * 0.1
    if 50 <= money_a <= 1000:
        money_b = money_a * 0.07
        money_c = money_a + money_b
        print(f"{money_c:.2f}")
main()
