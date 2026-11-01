from board import Board
from menue import Menu
from player import Player


class Game:
    WINNING_LINES = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()

        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit()

    def setup_players(self):
        for player in self.players:
            player.choose_name()

        self.players[0].choose_symbol()
        self.players[1].symbol = "O" if self.players[0].symbol == "X" else "X"
        print(f"{self.players[1].name} will play as {self.players[1].symbol}.")

    def play_game(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            print(f"{current_player.name}'s turn ({current_player.symbol})")

            position = self.get_position()
            if not self.board.update(position, current_player.symbol):
                print("Invalid move. Choose an available position.")
                continue

            if self.has_winner(current_player.symbol):
                self.board.display()
                print(f"{current_player.name} wins!")
                break

            if self.is_draw():
                self.board.display()
                print("It's a draw!")
                break

            self.current_player_index = 1 - self.current_player_index

        self.end_game()

    def get_position(self):
        while True:
            try:
                return int(input("Choose a position (1-9): "))
            except ValueError:
                print("Please enter a number from 1 to 9.")

    def has_winner(self, symbol):
        return any(
            all(self.board.cells[index] == symbol for index in line)
            for line in self.WINNING_LINES
        )

    def is_draw(self):
        return all(not cell.isdigit() for cell in self.board.cells)

    def end_game(self):
        choice = self.menu.display_end_menu()
        if choice == "1":
            self.board.reset()
            self.current_player_index = 0
            self.setup_players()
            self.play_game()
        else:
            self.quit()

    def quit(self):
        print("Thanks for playing!")


if __name__ == "__main__":
    Game().start_game()