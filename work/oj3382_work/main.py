"""3382"""
data = []
while True:
    s = input()
    if s == "NULL":
        break
    data.append(s)
for s in reversed(data):
    print(s)
