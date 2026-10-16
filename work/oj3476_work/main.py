"""3476"""

import json

n = int(input())

cats = {}
foxes = {}

for i in range(n):
    data = json.loads(input())

    for name, code in data.items():
        if code.startswith("Cat"):
            cats[code] = name
        elif code.startswith("Fox"):
            foxes[code] = name

if "Cat01" not in cats and "Garfield" not in foxes.values():
    cats["Cat01"] = "Garfield"

if "Fox01" not in foxes and "Fubuki" not in cats.values():
    foxes["Fox01"] = "Fubuki"

print("Cat :", len(cats))
print("Fox :", len(foxes))

for code in sorted(cats):
    print(cats[code], ":", code)

for code in sorted(foxes):
    print(foxes[code], ":", code)
