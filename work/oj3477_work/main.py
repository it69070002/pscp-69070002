"""3477"""
ingredients = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts"
}
flavors = {"Sweet", "Sour", "Salty"}
used = set()
taste = set()
while True:
    x = input()
    if x == "Cook":
        break
    used.add(x)
while True:
    x = input()
    if x == "End":
        break
    taste.add(x)
if not used.issubset(ingredients):
    print("This is not Pad Thai!!!")
elif used != ingredients:
    print("This is bad!")
elif taste != flavors:
    print("Not Bad...")
else:
    print("Delicious!")
