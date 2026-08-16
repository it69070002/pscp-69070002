"""3110"""
def main():
    """main"""
    a,b = input().upper().split()
    c = float(input())
    if a == "BKK" and b == "CNX":
        fee_sta = 10
        fee_wei = 30
    elif a == "CNX" and b == "UBP":
        fee_sta = 15
        fee_wei = 40
    elif a == "UBP" and b == "BKK":
        fee_sta = 20
        fee_wei = 40
    elif a == "BKK" and b == "PKT":
        fee_sta = 25
        fee_wei = 50
    elif a == "PKT" and b == "CNX":
        fee_sta = 30
        fee_wei = 60
    elif a == "UBP" and b == "PKT":
        fee_sta = 40
        fee_wei = 70
    else:
        print("Error")
        return
    total = fee_sta + (fee_wei * c)
    print(f"{total:.2f}")
main()
