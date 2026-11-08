"""3544"""
stock = {}
while True:
    data = input().split()
    command = data[0]
    if command == "END":
        break
    elif command == "ADD":
        name = data[1]
        amount = int(data[2])
        if name not in stock:
            stock[name] = 0
        stock[name] += amount
    elif command == "REMOVE":
        name = data[1]
        amount = int(data[2])
        if name not in stock:
            stock[name] = 0
        if stock[name] < amount:
            stock[name] = 0
            print("Not enough stock for", name)
        else:
            stock[name] -= amount
    elif command == "CHECK":
        names = sorted(stock)
        found = False
        for name in names:
            if stock[name] < 5:
                print(name)
                found = True
        if found == False:
            print("All stocks are sufficient")
    elif command == "REPORT":
        names = sorted(stock, reverse=True)
        for name in names:
            print(name + ":", stock[name])
