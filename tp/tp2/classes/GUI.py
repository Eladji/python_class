from classes.FleetManager import FleetManager

class GUI:
    def __init__(self, back_end: FleetManager):
        self.back_end = back_end
        self.__index = None

    @property
    def _index(self):
        return self.__index

    @_index.setter
    def _index(self, value):
        self.__index = value

    def clear_screen(self):
        """Clears the console screen for better readability."""
        print("\033[H\033[J", end="")

    def print_centered(self, text, width):
        """Prints text centered based on the given width."""
        print(text.center(width))

    def dynamic_border(self, width):
        """Creates a dynamic border based on the UI width."""
        print("=" * width)

    def main_ui(self, width, height):
        self.clear_screen()
        self.dynamic_border(width)
        self.print_centered("Welcome to the Space Fleet Management System", width)
        self.dynamic_border(width)
        print("\n" + " " * ((width // 2) - 10) + "1. Member")
        print(" " * ((width // 2) - 10) + "2. Ship")
        print(" " * ((width // 2) - 10) + "3. Fleet")
        print(" " * ((width // 2) - 10) + "4. Exit")
        print("\nChoose an option: ", end="")
        self._index = input()

        match self._index:
            case "1":
                self.member_ui(width, height)
            case "2":
                self.ship_ui(width, height)
            case "3":
                self.fleet_ui(width, height)
            case "4":
                print("Goodbye!")
                exit()
            case _:
                print("Invalid option")
                self.main_ui(width, height)

    def member_ui(self, width, height):
        self.clear_screen()
        self.dynamic_border(width)
        self.print_centered("Member Management", width)
        self.dynamic_border(width)
        print("\n" + " " * ((width // 2) - 15) + "1. Add Member")
        print(" " * ((width // 2) - 15) + "2. Edit Member")
        print(" " * ((width // 2) - 15) + "3. Delete Member from Ship")
        print(" " * ((width // 2) - 15) + "4. Delete Member 💀")
        print(" " * ((width // 2) - 15) + "5. List Members")
        print(" " * ((width // 2) - 15) + "6. Exit")
        print("\nChoose an option: ", end="")
        self._index = input()

        match self._index:
            case "1":
                self.back_end.add_member()
            case "2":
                self.back_end.edit_member_ui()
            case "3":
                self.delete_member_ui()
            case "4":
                self.back_end.remove_entity()
            case "5":
                self.list_member_ui()
            case "6":
                print("Returning to main menu...")
                self.main_ui(width, height)
            case _:
                print("Invalid option")
                self.member_ui(width, height)

    def ship_ui(self, width, height):
        self.clear_screen()
        self.dynamic_border(width)
        self.print_centered("Ship Management", width)
        self.dynamic_border(width)
        print("\nFeature under construction...")
        input("Press Enter to return to the main menu...")
        self.main_ui(width, height)

    def fleet_ui(self, width, height):
        self.clear_screen()
        self.dynamic_border(width)
        self.print_centered("Fleet Management", width)
        self.dynamic_border(width)
        print("\nFeature under construction...")
        input("Press Enter to return to the main menu...")
        self.main_ui(width, height)

    def init_ui(self, width, height):
        self.main_ui(width, height)
