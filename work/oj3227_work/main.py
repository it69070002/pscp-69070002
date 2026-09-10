"""3227"""
card = input().upper()
a = card[:-1]
b = card[-1]
if a == "A":
    a = "ace"
elif a == "J":
    a = "jack"
elif a == "Q":
    a = "queen"
elif a == "K":
    a = "king"
if b == "D":
    b = "diamonds"
elif b == "H":
    b = "hearts"
elif b == "S":
    b = "spades"
elif b == "C":
    b = "clubs"
print(a, "of", b)
