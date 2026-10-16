"""3478"""
s = input()
for ch in "abcdefghijklmnopqrstuvwxyz":
    lower_count = s.count(ch)
    upper_count = s.count(ch.upper())
    if lower_count > 0:
        print(f"{ch} = {lower_count}")
    if upper_count > 0:
        print(f"{ch.upper()} = {upper_count}")
