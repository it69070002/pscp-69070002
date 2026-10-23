"""3534"""
import ast
d = ast.literal_eval(input())
n = float(input())
count = 0
for k in sorted(d):
    if d[k] >= n:
        print(k, f"{d[k]:.2f}", sep="\t")
        count += 1
if not count:
    print("Nope")
