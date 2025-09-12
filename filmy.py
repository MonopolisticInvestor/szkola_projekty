class Film:
    def __init__(self, id, nazwa, cena):
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
            if lines[i] == '\n':
                continue
            else:
                if i == 3:
                    id = lines[0][3:].replace("\n", "")
                    nazwa = lines[1].replace("\n", "")
                    cena = lines[2].replace("\n", "")
                else:
                    id = lines[i - 2][3:].replace("\n", "")
                    nazwa = lines[i - 1].replace("\n", "")
                    cena = lines[i].replace("\n", "")

                if cena.find("pln") != -1:
                    film1 = Film(id, nazwa, cena)
                    self.listaFilmow.append(film1)

    def daneFilmow(self):
        for i in range(0, len(self.listaFilmow)):
            print("(" + str(self.listaFilmow[i].id) + "): " + str(self.listaFilmow[i].nazwa) + " " + self.listaFilmow[i].cena)

Wypozyczalnia1 = Wypozyczalnia()
Wypozyczalnia1.wczytajDane()

Wypozyczalnia1.daneFilmow()
