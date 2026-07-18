"""3040"""
coin_value = int(input())

c10 = coin_value // 10
c5 = (coin_value - (10*c10)) // 5
c2 = (coin_value - (10*c10) - (5*c5)) // 2
c1 = (coin_value - (10*c10) - (5*c5) - (2*c2))
print(f"10 = {c10}")
print(f"5 = {c5}")
print(f"2 = {c2}")
print(f"1 = {c1}")
