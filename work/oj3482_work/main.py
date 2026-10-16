"""3482"""

import sys

demons = {
    "Spider Demon": 1,
    "Swamp Demon": 2,
    "Arrow Demon": 1,
    "Hand Demon": 2,
    "Drum Demon": 3,
    "Mugen Train": 2,
    "Upper Moon": 3
}

killed = set()
total = 0

while len(killed) < 5:
    name = sys.stdin.readline()
    if not name:
        break

    name = name.strip()
    if name not in demons:
        continue

    target = demons[name]

    for attempt in range(3):
        print(target, flush=True)
        total += 1

        # รับผลจากกรรมการ
        result = sys.stdin.readline()
        if not result:
            sys.exit()

        result = result.strip()

        if result == "kill":
            print("kill", flush=True)
            killed.add(name)
            break

        if attempt == 2:
            print("back", flush=True)

print(total)
