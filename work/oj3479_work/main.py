"""3479"""
card = input().upper()
a = card[:-1]
b = card[-1]
if a == "A":
    a = "Ace"
elif a == "J":
    a = "Jack"
elif a == "Q":
    a = "Queen"
elif a == "K":
    a = "King"
if b == "D":
    b = "Diamonds"
elif b == "H":
    b = "Hearts"
elif b == "S":
    b = "Spades"
elif b == "C":
    b = "Clubs"
print(a, "of" ,b)
