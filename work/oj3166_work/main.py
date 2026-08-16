"""3166"""
def main():
    """main"""
    n = int(input())
    scores = []
    for _ in range(n):
        scores.append(int(input()))
    average = sum(scores) / n
    print(f"{average:.1f}")
    if min(scores) >= 50 and average >= 60.0:
        print("PASS")
    else:
        print("FAIL")
main()
