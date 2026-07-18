"""Colors"""
def main():
    """main"""
    co1 = input()
    co2 = input()
    if((co1) == "Red" and (co2) == "Yellow") or ((co1) == "Yellow" and (co2) == "Red"):
        color = "Orange"
    elif((co1) == "Red" and (co2) == "Blue") or ((co1) == "Blue" and (co2) == "Red"):
        color = "Violet"
    elif((co1) == "Yellow" and (co2) == "Blue") or ((co1) == "Blue" and (co2) == "Yellow"):
        color = "Green"
    elif(co1) == "Yellow" and (co2) == "Yellow":
        color = "Yellow"
    elif(co1) == "Blue" and (co2) == "Blue":
        color = "Blue"
    elif(co1) == "Red" and (co2) == "Red":
        color = "Red"
    else:
        color = "Error"
    print(color)
main()
