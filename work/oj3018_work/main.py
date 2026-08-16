"""3018"""
def main():
    """main"""
    a,b,c,d = [int(x) for x in input().split()]
    e,f,g,h = [int(x) for x in input().split()]
    width = (a,b,c,d)
    height = (e,f,g,h)
    if width > 0 and height > 0:
        area = width * height
    else:
        area = 0
    print(area)
main()
