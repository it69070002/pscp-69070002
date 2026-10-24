"""3537"""
import json
players = {}
dead = {}
while True:
    text = input()
    if text == "Start":
        break
    data = json.loads(text)
    players.update(data)
while True:
    text = input()
    if text == "End":
        break
    if text in players:
        dead[text] = players.pop(text)
impostor_count = list(players.values()).count("Impostor")
print(f"{impostor_count} Impostor Remains")
print("***Alive***")
for name in sorted(players.keys()):
    print(f"{name} : {players[name]}")
print("***Dead***")
for name in sorted(dead.keys()):
    print(f"{name} : {dead[name]}")
