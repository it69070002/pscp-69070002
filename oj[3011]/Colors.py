"""Colors"""
def main():
    """main"""
    color_a = input()
    color_b = input()
    if (color_a) == "Red" and (color_b) == "Yellow":
        color = "Orange"
    elif (color_a) == "Red" and (color_b) == "Blue":
        color = "Violet"
    elif (color_a) == "Yellow" and (color_b) == "Blue":
        color = "Green"
    elif (color_a) == "Yellow" and (color_b) == "Yellow":
        color = "Yellow"
    elif (color_a) == "Blue" and (color_b) == "Blue":
        color = "Blue"
    elif (color_a) == "Red" and (color_b) == "Red":
        color = "Red"
    else:
        color = "Error"
    print(color)
main()
