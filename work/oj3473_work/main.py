"""3473"""
s = input()
U = ["  *  ", " *** ", "* * *", "  *  ", "  *  "]
D = ["  *  ", "  *  ", "* * *", " *** ", "  *  "]
L = ["  *  ", " *   ", "*****", " *   ", "  *  "]
R = ["  *  ", "   * ", "*****", "   * ", "  *  "]
for i in range(5):
    for c in s:
        if c == 'U':
            print(U[i], end=" ")
        elif c == 'D':
            print(D[i], end=" ")
        elif c == 'L':
            print(L[i], end=" ")
        elif c == 'R':
            print(R[i], end=" ")
    print()
