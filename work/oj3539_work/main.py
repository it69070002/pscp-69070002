"""3539"""
model = input()
gb = input().replace(" ", "").upper()
if model == "iPhone 13 mini":
    if gb == "128GB":
        print(25900)
    elif gb == "256GB":
        print(29900)
    elif gb == "512GB":
        print(37900)
    else:
        print("Not Available")
elif model == "iPhone 13":
    if gb == "128GB":
        print(29900)
    elif gb == "256GB":
        print(33900)
    elif gb == "512GB":
        print(41900)
    else:
        print("Not Available")
elif model == "iPhone 13 Pro":
    if gb == "128GB":
        print(38900)
    elif gb == "256GB":
        print(42900)
    elif gb == "512GB":
        print(50900)
    elif gb == "1TB":
        print(58900)
    else:
        print("Not Available")
elif model == "iPhone 13 Pro Max":
    if gb == "128GB":
        print(42900)
    elif gb == "256GB":
        print(46900)
    elif gb == "512GB":
        print(54900)
    elif gb == "1TB":
        print(62900)
    else:
        print("Not Available")
else:
    print("Not Available")
