"""3392"""
arr = []
for i in range(3):
    n = int(input())
    arr.append(n)
    print("Input number", i + 1, "stored.")
for i in range(10):
    menu = int(input())
    if menu == 1:
        print("Original order:", *arr)
    elif menu == 2:
        print("Descending order:", *sorted(arr, reverse=True))
    elif menu == 3:
        print("Ascending order:", *sorted(arr))
    else:
        break
