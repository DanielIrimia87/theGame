from class_Games.cell import Cell
import random


# Clasa Grid reprezintă o grilă de joc pe care jucătorul poate să se deplaseze.
# Grila este o matrice de celule (Cell), fiecare celulă putând fi goală, un copac sau ținta.
# Grila gestionează plasarea copacilor și a țintei,
# și verifică dacă jucătorul încearcă să iasă de pe grilă.

# Atribute:

# size (int): Dimensiunea grilei (ex. 14 pentru o grilă de 14x14).
# cells (list of list of Cell): Matricea de celule care compune grila.
# target_x (int): Coordonata x a țintei.
# target_y (int): Coordonata y a țintei.

# Grid - Metode:
# Constructor care inițializează grila cu dimensiunea specificată (size) și plasează un număr de copaci (tree_count = 10).
# Metoda place_trees care primeste un parametru cu nr_copaci și plasează cantitatea de copacii pe grilă în poziții aleatorii.
# Metoda place_target, fara parametrii, plasează ținta pe grilă într-o poziție aleatorie.
# Metoda update_player_position primeste ca parametru un jucator (player). Verifică dacă jucătorul încearcă să iasă de pe grilă.
# Returnează False dacă jucătorul încearcă să iasă de pe grilă, altfel True, astea in functie de coordonatele jucatorului(x, y).
# Metoda print_grid care afișează grila și initiala jucătorului.

class Grid:
    def __init__(self, size):
        self.size = size  # Size of the grid
        # Initialize the grid with empty cells
        self.cells = []  # [[Cell() for _ in range(size)] for _ in range(size)]
        for row in range(size):
            # Create a new list for each row
            row_cell = []
            for col in range(size):
                # Create a new Cell object for each cell
                cell = Cell()
                # Add the cell to the row list
                row_cell.append(cell)
            # Add the row list to the grid
            self.cells.append(row_cell)

        self.target_x = 0  # X coordinate for the target
        self.target_y = 0  # Y coordinate for the target
        self.tree_count = 10  # Default number of trees

    def place_trees(self, nr_trees):
        placed_trees = 0
        while placed_trees < nr_trees:
            # Pick a random location on the grid
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            # If the cell is empty, place a tree there
            if self.cells[y][x].cell_type == Cell.EMPTY:
                self.cells[y][x] = Cell(Cell.TREE)
                placed_trees += 1

    def place_target(self):
        while True:
            # Pick a random location on the grid
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            # If the cell is empty, place the target there
            if self.cells[y][x].cell_type == Cell.EMPTY:
                self.cells[y][x] = Cell(Cell.TARGET)
                self.target_x = x
                self.target_y = y
                break

    def update_player_position(self, player):
        # Check if the player's position is within bounds of the grid
        if 0 <= player.x < self.size and 0 <= player.y < self.size:
            return True
        else:
            return False

    def print_grid(self, player):
        # Print the grid with the player's initial position
        for y in range(self.size):
            for x in range(self.size):
                if player.start_x == x and player.start_y == y:
                    print(player.name[0], end=' ')
                else:
                    print(self.cells[y][x].cell_type, end=' ')
            print()  # Newline for each row
