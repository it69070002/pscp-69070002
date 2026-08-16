"""3104"""
def main():
    """main"""
    age,day = input().split()
    age = int(age)
    if age < 5:
        money = 0
    elif age <= 18:
        money = 100
    else:
        money =150
    if day == "Wed":
        money //= 2
    print(money)
main()
