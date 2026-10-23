"""3537"""
alive = {}
dead = {}
while True:
    data = input()
    if data == "Start":
        break
    name, role = data.split()
    alive[name] = role
while True:
    name = input()
    if name == "End":
        break
    if name in alive:
        dead[name] = alive.pop(name)
count = 0
for role in alive.values():
    if role == "Impostor":
        count += 1
print(count, "Impostor Remains")
print("***Alive***")
for name in sorted(alive):
    print(name, alive[name])
print("***Dead***")
for name in sorted(dead):
    print(name, dead[name])
