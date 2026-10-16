"""3474"""
c1 = input()
c2 = input()
c3 = input()
c4 = input()
digits = {
    "Black": 0, "Brown": 1, "Red": 2, "Orange": 3,
    "Yellow": 4, "Green": 5, "Blue": 6,
    "Purple": 7, "Grey": 8, "White": 9
}
multiplier = {
    "Black": 1, "Brown": 10, "Red": 100,
    "Orange": 1000, "Yellow": 10000, "Green": 100000,
    "Blue": 1000000, "Purple": 10000000,
    "Gold": 0.1, "Silver": 0.01
}
tolerance = {
    "Brown": 1, "Red": 2, "Green": 0.5,
    "Blue": 0.25, "Purple": 0.10, "Grey": 0.05,
    "Gold": 5, "Silver": 10
}
try:
    value = (digits[c1] * 10 + digits[c2]) * multiplier[c3]
    tol = tolerance[c4] / 100
    lower = value * (1 - tol)
    upper = value * (1 + tol)
    print(f"{lower:.4f}")
    print(f"{upper:.4f}")
except (ValueError, KeyError):
    print("Error")
