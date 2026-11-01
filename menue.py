class Menu:
    def display_main_menu(self):
        print("Welcome to X-O game")
        print("1. Start game")
        print("2. Quit")

        return self._get_choice("Choose an option: ")

    def display_end_menu(self):
        print("Game over")
        print("1. Restart")
        print("2. Quit")

        return self._get_choice("Choose an option: ")

    def _get_choice(self, prompt):
        while True:
            choice = input(prompt).strip()
            if choice in ["1", "2"]:
                return choice
            else:
                print("Invalid choice. Enter 1 or 2.")