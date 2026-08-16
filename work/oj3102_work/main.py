"""3102"""
def main():
    """main"""
    year = int(input())
    side = int(input())
    if year <= 1990:
        if side <= 1500:
            print("1250")
        elif side > 2000:
            print("2000")
        else:
            print("1400")
    elif year >= 2000:
        if side <= 1500:
            print("1000")
        elif side > 2000:
            print("1500")
        else:
            print("1200")
    else:
        if side <= 1500:
            print("1100")
        elif side > 2000:
            print("1700")
        else:
            print("1300")
main()
