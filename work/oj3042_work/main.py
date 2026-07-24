"""3042"""
def main():
    """main"""
    number_a = int(input())
    number_a = number_a // 10 * 10
    for i in range(number_a,-1,-10):
        print(i,end=" ")
main()
