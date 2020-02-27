class Lunch:
    def __init__(self, menu):
        self.menu = menu

    def menu_price(self):

        choice = self.menu
        if choice == "menu1":
            print("Your choice - " + choice + " - Price 12.00")
        elif choice == "menu2":
            print("Your choice - " + choice + " - Price 13.40")
        else:
            print("Error in menu")

Paul = Lunch("menu1")
Paul.menu_price()

