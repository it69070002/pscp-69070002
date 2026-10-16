"""3355"""
nums = []
while True:
    n = int(input())
    if n == -1:
        break
    nums.append(n)
i = 0
result = []
while i < len(nums):
    start = nums[i]
    end = start
    while i + 1 < len(nums) and nums[i + 1] == end + 1:
        i += 1
        end = nums[i]
    if start == end:
        result.append(str(start))
    else:
        result.append(str(start) + "-" + str(end))
    i += 1
print(", ".join(result))
