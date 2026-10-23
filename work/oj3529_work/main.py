"""3529"""
s = input()
for n in range(26):
    text = ""
    for c in s:
        if 'a' <= c <= 'z':
            text += chr((ord(c) - 97 - n) % 26 + 97)
        elif 'A' <= c <= 'Z':
            text += chr((ord(c) - 65 - n) % 26 + 65)
        else:
            text += c
    if "the" in text.lower().split():
        print(text)
        break
