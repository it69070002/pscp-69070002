"""3020"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if not d:
        print(0)
    elif not b:
        print(a * d)
    else:
        discount = (d - 1) // b
        answer = (d - discount) * a + discount * c
        print(answer)
main()
