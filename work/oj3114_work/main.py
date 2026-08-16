"""3114"""
def main():
    """main"""
    park_car = int(input())
    out_car = int(input())
    for x in range(park_car,out_car):
        if x == 1:
            print(25)
        elif x == 2:
            print(50)
        elif x == 3:
            print(80)
        elif x == 4:
            print(110)
        elif x == 5:
            print(145)
        elif x == 6:
            print(180)
        elif 7 <= x <= 24:
            print(250)
        else:
            print("ERROR")
main()
