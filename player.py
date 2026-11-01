class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            user_name = input("Enter your name: ").strip()
            if user_name.isalpha():
                self.name = user_name
                break
            else:
                print("Invalid name. Use letters only.")

    def choose_symbol(self):
        while True:
            user_symbol = input("Please enter your symbol (X or O): ").upper()
            if user_symbol in ["X", "O"]:
                self.symbol = user_symbol
                break
            else:
                print("Invalid symbol. Choose X or O.")