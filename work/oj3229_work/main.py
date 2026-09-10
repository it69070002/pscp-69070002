"""3229"""
def main():
    """main"""
    point_a = int(input())
    point_bonut = int(input())
    day = int(input())
    total = point_a + point_bonut
    if day > 3:
        total = total * 1.5
    if total >= 1500:
        rank = 5
    elif total >= 1000:
        rank = 4
    elif total >= 500:
        rank = 3
    elif total >= 200:
        rank = 2
    else:
        rank = 1
    if rank == 5 and day >= 7:
        status = 99
    elif rank == 4 and point_bonut > 300:
        status = 88
    else:
        status = 0
    print(int(total))
    print(rank)
    print(status)
main()
