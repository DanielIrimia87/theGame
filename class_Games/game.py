#### 5. Clasa Game gestionează logica principală a jocului, inclusiv inițializarea jocului, interacțiunea cu jucătorul și verificarea stării jocului.

# Atribute:
# * Un player (Player): Obiectul jucătorului.
# * Un grid (Grid): Obiectul grilei de joc.

# Metode:
# Constructor care inițializează jocul dand o valoare nula playerului și creează grila,
#       apeland constructorul clasei Grid cu dimensiunile corespunzatoare(14x14)
# Metoda start care începe jocul: printeaza un mesaj de bun venit,
#   explica sumar regulile jocului și scopul jucatorului.
#   Apoi solicită numele jucătorului și creaza un player cu numele introdus și in functie de dimensiunea
#   grilei calculeaza coordonatele jucatorului: acesta trebuie sa se afle in centrul grilei.
# * Apoi apeleaza metoda play.

from grid import Grid
from player import Player


class Game:
    def __init__(self):
        self.player = None
        self.grid = Grid(14)

    def start(self):
        print("Welcome to the game!")
        print("The rules are simple. Use 'W', 'A', 'S', 'D' to move.")
        print("Try to reach the 'X' to win. Don't go outside the grid or you'll lose.")
        player_name = input("Please enter your name: ")
        # Calculate the starting position to be in the center of the grid
        start_x = self.grid.size // 2
        start_y = self.grid.size // 2
        # Create a player with the name entered and calculated start position
        self.player = Player(player_name, start_x, start_y)
        # Call the play method to start the game loop
        self.play()

    def play(self):
        while True:
            self.grid.print_grid(Player)
            direction = input("Enter direction (w, a, s, d): ").lower()
            player_moved = self.player.move(direction)
            message = self.player.move(direction)

            if not player_moved:
                print(message)
                continue

            # if self.grid.update_player_position(self.player):
            #     if self.grid.is_out_of_bounds(self.player):
            #         print("You have moved out of bounds! Game over.")
            #         break
            #     else:
            #         self.player.update_score(1)  # Add points for a valid move
