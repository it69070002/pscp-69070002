"""3603"""
a = int(input())
b = int(input())
rabbit = b // 2 - a
bird = a - rabbit
if b % 2 or rabbit < 0 or bird < 0:
    print("Impossible")
else:
    print(rabbit, bird)
