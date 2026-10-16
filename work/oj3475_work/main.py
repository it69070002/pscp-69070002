"""3475"""
menu = []
while True:
    x = input()
    if x == "DONE":
        break
    if x == "CLOSED":
        menu = []
        break
    if x == "SOMETHING'S WRONG":
        menu = []
    elif x.startswith("Can't do: "):
        food = x.replace("Can't do: ", "")
        if food in menu:
            menu.remove(food)
    else:
        food, course = x.rsplit(" #", 1)
        if course == "N":
            menu.append(food)
        else:
            menu.insert(int(course) - 1, food)
print("Full Course:", menu, "Reversed:", menu[::-1])
