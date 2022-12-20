from entities import Character
from errors import InvalidCommand

class Menu:
    def print_menu(self):
        print("1. Create a new character")

    def command_create_character(self, name, sex, ch_class):
        pass

    def run(self):
        # infinite menu loop
        while True:  
            # print the menu
            # ...

            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")

            # catch errors
            try:
                # process the user's choice
                if choice == "1":                    
                    # ask the user to input the necessary command parameters
                    name = input("Enter the character name (alpha-numeric): ")

                    # ...

                    # char = self.command_create_character(....)
                    
                    # ...
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()
