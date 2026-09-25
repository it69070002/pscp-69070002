"""3384"""
import json
def main():
    """main"""
    a = json.loads(input())
    b = False
    for i in a:
        if not i % 2:
            print(i)
            b = True
    if not b:
        print("Nope")
main()
