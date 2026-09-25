"""3297"""
n = int(input())
ans = []
for _ in range(100):
    try:
        age, ticket = map(int, input().split())
    except EOFError:
        break
    if age < 15:
        ans.append("-1")
    elif ticket > n:
        ans.append("-2")
    else:
        if age <= 22:
            PRICE = 120
        elif age >= 60:
            PRICE = 75
        else:
            PRICE = 150
        n = n - ticket
        ans.append(str(PRICE * ticket) + " " + str(n))
    if not n:
        break
print("\n".join(ans))
