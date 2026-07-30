"""3072"""
def main():
    """main"""
    name = input().lower()
    for x in "aeiou":
        count = name.count(x)
        if count > 0:
            print(f"{x} : {count}")
main()
