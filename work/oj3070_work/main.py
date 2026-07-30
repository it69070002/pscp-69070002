"""3070"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    text = [a,b,c]
    even,odd = 0,0
    for i in text:
        if i % 2:
            i += 1
            print(even)
    else:
        print(odd)
main()
