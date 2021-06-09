from dotenv import load_dotenv
import os
load_dotenv('.env')

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.name + " available from " + str(self.start_time) + " to " + str(self.end_time)

    def calculate_bill(self, purchased_items):
        total_bill = 0
        for item in purchased_items:
            total_bill += self.items.get(item)

        return total_bill

brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,'tea': 1.00,'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

early_bird = Menu("early bird", {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

dinner = Menu("dinner", {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

kids = Menu("kids", {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_bird.calculate_bill(['duck ragu', 'coffee']))
# print(kids)


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):

        if time >= 11 and time < 15:
            return [brunch, kids]
        elif time >=15 and time <= 16:
            return [brunch, kids, early_bird]
        elif time >16 and time < 17:
            return [early_bird, kids]
        elif time >= 17 and time <=18:
            return [dinner, early_bird, kids]
        elif time >18 and time <=21:
            return [dinner, kids]
        elif time > 21 and time <=23:
            return [dinner]



flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

