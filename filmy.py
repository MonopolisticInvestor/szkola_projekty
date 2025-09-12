class Film:
    def _init_(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa,
        self.cena = cena

class Wypozyczalnia:
    def __init__(self):
        self.listaFilmow = []
    
    def wczytajDane(self):
        file = open("filmy.txt")

        lines = file.readlines()
        for i in range(0, len(lines)):
            if (lines[i] == '\n'):
                continue
            else:
                if (i == 3):
                    id = lines[0][3:].replace("\n", "")
                    nazwa = lines[1].replace("\n", "")
                    cena = lines[2].replace("\n", "")
                else:
                    id = lines[i - 2][3:].replace("\n", "")
                    nazwa = lines[i - 1].replace("\n", "")
                    cena = lines[i].replace("\n", "")

                film1 = Film(id, nazwa, cena)
                self.listaFilmow.append(film1)

    def daneFilmow(self):
        print("1")

Wypozyczalnia1 = Wypozyczalnia()
Wypozyczalnia.wczytajDane()