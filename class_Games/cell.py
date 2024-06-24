# Construieste o clasa care sa se numeasca Cell. Aceasta are 3 atribute constante: empty ‘.’ , target ‘X’ și tree ‘T’.
# Aceasta clasa are un constructor explicit care primeste un parametru numit cell_type cu valoare predefinita* empty.

class Cell():
    EMPTY = '.'
    TARGET = 'X'
    TREE = 'T'

    def __init__(self, cell_type=EMPTY):
        self.cell_type = cell_type


cel = Cell()

print(cel.TREE)