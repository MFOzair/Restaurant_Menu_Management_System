# Class representing a menu with its items and time of availability
class Menu:
    def __init__(self, name, items, start_time, end_time):
        # Initialize menu name, items (as a dictionary), and start/end time
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # String representation of the menu, showing its name and availability time
    def __str__(self):
        return(f"You are looking at the {self.name} Menu, available from {self.start_time} to {self.end_time}")

    # Method to calculate the total bill for purchased items
    def calculate_bill(self, purchased_items):
        bill = 0
        # Loop through purchased items and add the corresponding price from the menu
        for item in purchased_items:
            if item in self.items:
                bill += self.items[item]
        return f"You bought {purchased_items} \nYour total bill is: {bill}"


# Instances of the Menu class
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 
                         'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 
                         'orange juice': 3.50}, 11, 16)

early_bird = Menu("Early-bird Dinners", {'salumeria plate': 8.00, 'salad and breadsticks': 14.00, 
                                         'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
                                         'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 
                                         'espresso': 3.00}, 15, 18)

dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
                         'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
                         'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)

kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

arepas_menu = Menu("Take a’ Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 
                                     'jamon arepa': 7.50}, 10, 20)

# Print bill for purchased items
print(brunch.calculate_bill(["pancakes", "waffles"]))


# Class representing a restaurant franchise, containing multiple menus
class Franchise:
    def __init__(self, address, menus):
        # Initialize franchise address and a list of available menus
        self.address = address
        self.menus = menus

    # String representation of the franchise
    def __str__(self):
        return f"Restaurant address: {self.address}"

    # Method to display available menus at a given time
    def available_menus(self, time):
        for a_menu in self.menus:
            # Check if the menu is available during the given time
            if a_menu.start_time <= time < a_menu.end_time:
                print(f"Available menu: {a_menu.name}")


# Creating franchise instances with the defined menus
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [brunch, early_bird, dinner, kids])

# Check available menus at a specific time (15 means 3 PM)
flagship_store.available_menus(15)


# Class representing a business containing multiple franchise locations
class Business:
    def __init__(self, name, franchises):
        # Initialize business name and list of franchise locations
        self.name = name
        self.franchises = franchises

# Creating a business instance with franchises
flagship_store = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
new_business = Business("Take a' Arepa", [flagship_store, new_installment, arepas_place])

