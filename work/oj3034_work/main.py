"""3034"""
def main():
    """main"""
    n,k = map(int, input().split())
    cnt = [0] * k
    for _ in range(n):
        row = int(input())
        cnt[row - 1] += 1
    trips = min(cnt)
    answer = n - trips * k
    print(answer)
main()
