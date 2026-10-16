"""3483"""

N, M = map(int, input().split())

if not (1 <= N <= 10 and 1 <= M <= 20):
    print("Data Incorrect")
else:
    teams = []
    total = 0
    valid = True

    for i in range(N):
        scores = list(map(int, input().split()))

        if len(scores) != M or any(s < 0 or s > 100 for s in scores):
            valid = False

        teams.append(scores)

    if not valid:
        print("Data Incorrect")
    else:
        for i in range(N):
            scores = teams[i]
            average = sum(scores) / M
            maximum = max(scores)
            total += sum(scores)

            print(f"Team {i + 1}: Average = {average:.2f}, Max = {maximum}")

        print(f"Total Score of All Teams = {total}")
