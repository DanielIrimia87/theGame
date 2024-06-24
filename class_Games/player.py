# 3. Scrie o clasa care se numeste player. In metoda constructor aceasta primeste 3 parametrii: nume, start_x și start_y.
# Numele jucatorului și pozitia initiala exprimata prin coordonate (x, y).
# Pe langa aceasta se initializeaza la 0 inca doua atribute cu privire la punctajul jucatorului: score și numărul de miscari: moves.
# Singura metoda a clase, in afara constructorului, este metoda move care primid o directie: sus, jos,
# stanga sau dreapta (w, s, a, d) actualizeaza pozitia actuala a jucatorului (x și y)
# adaugand o unitate in directia specificata de parametrul direction.


class Player():
    def __init__(self, name, start_x, start_y):
        self.name = name
        self.start_x = start_x
        self.start_y = start_y
        self.score = 0
        self.moves = 0

    def move(self, direction):

        if direction == 'w':  # up
            self.start_y += 1
        elif direction == 's':  # down
            self.start_y -= 1
        elif direction == 'a':  # left
            self.start_x -= 1
        elif direction == 'd':  # right
            self.start_x += 1
        else:
            print('Te rog foloseste W, S, A, D ')
