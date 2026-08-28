"""3290"""
def main():
    """main"""
    k = int(input())
    n = int(input())
    for i in range(k):
        if n % 2 != 0:
            kn = n // 2
            print("*", end="")            
main()
