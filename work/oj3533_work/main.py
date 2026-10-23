"""3533"""
s = input()
for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    n = s.count(c)
    if n > 0:
        re = ""
        for i in range(n):
            if i > 0 and not i % 5:
                re += "|"
            re += "-"
        print(c, ":", re)
