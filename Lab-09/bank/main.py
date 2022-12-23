from bank import Bank, Account, User, InvalidCommand

class Menu:
    def print_menu(self):
        print("1. Register a new user")
        print("7. Exit")

    def run(self):
        # create a new bank
        # ...

        # infinite menu loop
        while True:  
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":
                    names = input("Enter the user's names (alpha-only): ")
                    
                    #...

                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()
