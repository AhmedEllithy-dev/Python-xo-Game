class Board:
    def __init__(self):
        self.cells = [str(number) for number in range(1, 10)]

    def display(self):
        print(f"\n {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print("---|---|---")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("---|---|---")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} \n")

    def is_valid_move(self, position):
        return 1 <= position <= 9 and self.cells[position - 1].isdigit()

    def update(self, position, symbol):
        if self.is_valid_move(position):
            self.cells[position - 1] = symbol
            return True
        return False

    def reset(self):
        self.cells = [str(number) for number in range(1, 10)]