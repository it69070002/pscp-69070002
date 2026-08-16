"""3108"""
def main():
    """main"""
    pencil,book,color_box = [int(x) for x in input().split()]
    n = pencil + book + color_box
    total = pencil * 25 + book * 40 + color_box * 55
    if n >= 3:
        total = total * 90 // 100
    print(total)
main()
