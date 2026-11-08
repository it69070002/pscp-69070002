"""3645"""
phone = input()
country = input()

if country == "Domestic":
    if len(phone) == 10:
        print(phone[:2] + " " + phone[2:6] + " " + phone[6:])
    else:
        print(phone[0] + " " + phone[1:5] + " " + phone[5:])
else:
    if len(phone) == 10:
        print("+66" + phone[1:2] + " " + phone[2:6] + " " + phone[6:])
    else:
        print("+66 " + phone[1:5] + " " + phone[5:])
