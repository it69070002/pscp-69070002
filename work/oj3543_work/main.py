"""3543"""
n = int(input())
prime = True
if n < 2:
    prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            prime = False
            break
if prime:
    print("Yes")
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
else:
    print("No")
