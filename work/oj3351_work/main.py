"""3351"""
s = input().upper()
n = len(s)

if all(c in "IT" for c in s):
    print("unknown", n)
else:
    i = 0
    max_a = 0

    while i < n:
        if s[i] == 'R':
            if i + 1 == n or s[i + 1] != 'A':
                print("no", i)
                break

            j = i + 1
            while j < n and s[j] == 'A':
                j += 1

            max_a = max(max_a, j - i - 1)
            i = j

        elif s[i] == 'A':
            print("no", i)
            break

        elif s[i] == 'B':
            if i + 1 == n or s[i + 1] not in "IT":
                print("no", i)
                break

            i += 1
            while i < n and s[i] in "IT":
                i += 1

        elif s[i] in "IT":
            i += 1

        else:
            print("no", i)
            break
    else:
        print("yes", max_a)
