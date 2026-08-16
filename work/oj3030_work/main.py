"""3030"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    h = int(input())
    day1 = (a + e - 1) // e
    day2 = (b + f - 1) // f
    day3 = (c + h - 1) // h
    day4 = (d + g - 1) // g
    print(max(day1, day2, day3, day4))
main()
