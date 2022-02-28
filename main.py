from datetime import datetime
from string import ascii_letters, digits
from random import choices


class Parking:
    def __init__(self):
        self.spots = {}

    def get_ticket(self):
        start_time = datetime.now()
        self.key = ''.join(choices(ascii_letters + digits, k=8))
        self.spots.update(
            {self.key: {"start": start_time,
                        "locked": True}
             })

    def calculator(self, money: float):
        entered = 0
        while entered < money:
            change = int(input("$~ "))
            entered += change
        if entered > money:
            print(f"change = {entered - money}")
            return True
        else:
            return True

    def payment(self, consumed):
        if consumed <= 15:
            return True
        elif 15 < consumed <= 120:
            price = round((consumed / 60) * 2, 2)
            print(f"the amount is : {price}")
            if self.calculator(price):
                return True
        else:
            price = round((((consumed - 120) / 60) * 5) + 2 * 2, 2)
            print(f"the amount is : {price}")
            if self.calculator(price):
                return True

    def validate(self):
        end_time = datetime.now()
        delta_time = end_time - self.spots[self.key]["start"]
        in_min = delta_time.total_seconds() // 60
        if self.payment(in_min):
            self.spots[self.key]["locked"] = False

    def open_gate(self):
        if not self.spots[self.key]["locked"]:
            print("gate opened")
        else:
            print("please pay your ticket")


# if __name__ == '__main__':
#     p = Parking()
#     p.get_ticket()
#     p.validate()
#     p.open_gate()
