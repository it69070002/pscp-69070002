"""จำนวนสระ"""
def main():
    """3103"""
    name = int(input())
    count = 0
    for _ in range(name):
        ch = input().upper()
        if ch in "AEIOU":
            count += 1
    print(count)
main()
