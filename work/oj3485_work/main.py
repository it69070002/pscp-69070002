"""3485"""
_ = int(input())
arr = list(map(int, input().split()))
result = []
for x in arr:
    if arr.count(x) == 1:
        result.append(x)
result.sort()
print(*result)
