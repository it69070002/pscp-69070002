"""Colors"""
def main():
    """main"""
    colora = input()
    colorb = input()
    if ((colora) == "Red" and (colorb) == "Yellow") or ((colora) == "Yellow" and (colorb) == "Red"):
        color = "Orange"
    elif ((colora) == "Red" and (colorb) == "Blue") or ((colora) == "Blue" and (colorb) == "Red"):
        color = "Violet"
    elif ((colora) == "Yellow" and (colorb) == "Blue") or ((colora) == "Blue" and (colorb) == "Yellow"):
        color = "Green"
    elif (colora) == "Yellow" and (colorb) == "Yellow":
        color = "Yellow"
    elif (colora) == "Blue" and (colorb) == "Blue":
        color = "Blue"
    elif (colora) == "Red" and (colorb) == "Red":
        color = "Red"
    else:
        color = "Error"
    print(color)
main()
