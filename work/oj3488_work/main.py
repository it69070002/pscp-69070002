"""3488"""
demons = {
    "Spider Demon": 1,
    "Swamp Demon": 2,
    "Arrow Demon": 1,
    "Hand Demon": 2,
    "Drum Demon": 3,
    "Mugen Train": 2,
    "Upper Moon": 3
}
kills = 0
total = 0
order = list(demons.keys())
index = 0
while kills < 5:
    name = order[index % len(order)]
    print(name, flush=True)
    attempts = 0
    while attempts < 2:
        a = int(input())
        total += 1
        attempts += 1
        if a == demons[name]:
            print("kill", flush=True)
            kills += 1
            break
    if attempts == 2 and a != demons[name]:
        print("back", flush=True)
    index += 1
print(total)
