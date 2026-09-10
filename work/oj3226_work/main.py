"""3226"""
import math
def main():
    """main"""
    n = float(input())
    k = int(input())
    current_price = n
    for _ in range(k):
        increase = current_price * 0.0381
        increase_truncated = math.floor(increase * 100) / 100
        current_price += increase_truncated
    print(f"{current_price:.2f}")
main()
