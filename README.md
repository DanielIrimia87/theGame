# The Game Project 1.0
## Project python game
* Vezi sesiunea de functii pentru detalii despre parametrii cu valori predefinite.

###### 1. Creati un nou proiect pycharm numit theGameProject. Acesta trebuie sa aiba virtual environment.

    * Jucătorul controlează un caracter pe o grilă de 14x14 folosind tastele 'W', 'A', 'S', 'D'. La începutul jocului,
      grila este afișată cu puncte ('.') și copaci ('C'). În grilă este plasată aleatoriu o țintă ('X'), care este
      vizibilă. Jucătorul trebuie să ajungă la țintă pentru a câștiga jocul. Dacă jucătorul încearcă să iasă de pe grid,
      jocul se încheie și jucătorul pierde. Jucătorul primește 5 puncte pentru fiecare mișcare. La sfârșit, dacă
      jucătorul câștigă jocul, este felicitat și i se printeaza și cantitatea de puncte.

###### 2. Construieste o clasa care sa se numeasca Cell. Aceasta are 3 atribute constante: empty ‘.’ , target ‘X’ și tree ‘T’.
    * Aceasta clasa are un constructor explicit care primeste un parametru numit cell_type cu valoare predefinita*
      empty.

###### 3. Scrie o clasa care se numeste player. In metoda constructor aceasta primeste 3 parametrii: nume, start_x și start_y.

* Numele jucatorului și pozitia initiala exprimata prin coordonate (x, y). Pe langa aceasta se initializeaza la 0 inca
  doua atribute cu privire la punctajul jucatorului: score și numărul de miscari: moves.


* Singura metoda a clase, in afara constructorului, este metoda move care primid o directie: sus, jos, stanga sau
  dreapta (w, s, a, d) actualizeaza pozitia actuala a jucatorului (x și y) adaugand o unitate in directia specificata de
  parametrul direction.

###### 4. Clasa Grid reprezintă o grilă de joc pe care jucătorul poate să se deplaseze. Grila este o matrice de celule (Cell),

* fiecare celulă putând fi goală, un copac sau ținta. Grila gestionează plasarea copacilor și a țintei, și verifică
  dacă jucătorul încearcă să iasă de pe grilă.

Atribute:

* size (int): Dimensiunea grilei (ex. 14 pentru o grilă de 14x14).
* cells (list of list of Cell): Matricea de celule care compune grila.
* target_x (int): Coordonata x a țintei.
* target_y (int): Coordonata y a țintei.

Metode:

* Constructor care inițializează grila cu dimensiunea specificată (size) și plasează un număr de copaci (
  tree_count = 10).
* Metoda place_trees care primeste un parametru cu nr_copaci și plasează cantitatea de copacii pe grilă în poziții
  aleatorii.
* Metoda place_target, fara parametrii, plasează ținta pe grilă într-o poziție aleatorie.
* Metoda update_player_position primeste ca parametru un jucator (player). Verifică dacă jucătorul încearcă să iasă
  de pe grilă.
* Returnează False dacă jucătorul încearcă să iasă de pe grilă, altfel True, astea in functie de coordonatele
  jucatorului(x, y).
* Metoda print_grid care afișează grila și initiala jucătorului.

###### 5.1 Clasa Game gestionează logica principală a jocului, inclusiv inițializarea jocului, interacțiunea cu jucătorul și verificarea stării jocului.

Atribute:
* Un player (Player): Obiectul jucătorului.
* Un grid (Grid): Obiectul grilei de joc.

Metode:
* Constructor care inițializează jocul dand o valoare nula playerului și creează grila, apeland constructorul clasei Grid 
* cu dimensiunile corespunzatoare(14x14)
* Metoda start care începe jocul: printeaza un mesaj de bun venit, explica sumar regulile jocului și scopul jucatorului. 
* Apoi solicită numele jucătorului și creaza un player cu numele introdus și in functie de dimensiunea grilei calculeaza 
* coordonatele jucatorului: acesta trebuie sa se afle in centrul grilei. 
* Apoi apeleaza metoda play.

###### 5.2 Metoda play este  contine game loop-ul (un while True) din care iesim atunci cand jucatorul a castigat sau a pierdut folosind instructiunea break.

* In acest loop la inceput se va printa grila apeland metoda corespunzatoare din clasa Grid. 
* Apoi se cere ca jucatorul sa introduca directia de deplasare a jucatorului (w, a, s, d) și cu aceasta informatie 
* se misca jucatorul apeland metoda pentru miscarea jucatorului din clasa Player.
* Folosind metoda update_player_position se verifica daca jucatorul a iesit de pe grila sau nu.
* Apoi trebuie verificat daca noua pozitie corespunde unui copac se anunta ca miscarea nu este valida și se muta jucatorul in pozitia precedenta. 
* Bonus: actualizeaza și punctele din scor
* Daca, in schimb, noua pozitie este cea a targetului jucatorul a castigat se felicita și se printeaza scorul.









