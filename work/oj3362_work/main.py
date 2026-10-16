"""3362"""
a = input().lower()
b = input().lower()
while len(a) < len(b):
    a += a[0]
while len(b) < len(a):
    b += b[0]
s = ""
for i, ch in enumerate(a):
    if ch in "love" or b[i] in "love":
        s += "w"
    else:
        s += "$"
N = s.count("w")
if N % 2 == 1:
    s += str(max(len(x) for x in s.split("$")))
elif "ww" not in s:
    s += "#"
print(s)
