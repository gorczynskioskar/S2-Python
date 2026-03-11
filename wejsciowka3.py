class Instrument:
    __skala_dzwiekow=""

    def __init__(self, nazwa: str, typ: str):
        self.nazwa=nazwa
        self.typ=typ

    def dodaj_dzwiek(self, dzwiek: str):
        if self.__skala_dzwiekow == "":
            self.__skala_dzwiekow=dzwiek
        else:
            self.__skala_dzwiekow=self.__skala_dzwiekow+" "+dzwiek

    @staticmethod
    def czy_instrument(object):
        if isinstance(object, Instrument):
            return True
        else:
            return False
    def opis(self):
        return f"{self.nazwa} ({self.liczba_strun} strun) − dzwieki: {self.__skala_dzwiekow}"
    def __len__(self):
        return len(self.__skala_dzwiekow.split())
    def __str__(self):
        return self.opis()
    def get_skala_dzwiekow(self):
        return self.__skala_dzwiekow


class Gitara(Instrument):
    liczba_strun=0
    def __init__(self, nazwa: str, typ: str, liczba_strun: int):
        super().__init__(nazwa, typ)
        self.liczba_strun=liczba_strun
    def __add__(self, other):
        if isinstance(other, Gitara):
            nowa_gitara= Gitara(self.nazwa,self.typ, self.liczba_strun)
            nowa_gitara.dodaj_dzwiek(self.get_skala_dzwiekow())
            nowa_gitara.dodaj_dzwiek(other.get_skala_dzwiekow())
            return nowa_gitara
        else:
            raise TypeError("Można dodawać tylko obiekty klasy Gitara")


#zad1
i = Instrument("Flet","Dety")
i.dodaj_dzwiek("C4")
i.dodaj_dzwiek("D4")
print(Instrument.czy_instrument(i)) # True
print(Instrument.czy_instrument('a')) # F al s e
print()
#zad2
g = Gitara("Gitara_klasyczna","Strunowy",6)
g.dodaj_dzwiek("E2")
g.dodaj_dzwiek("A2")
print(g.opis()) #Gitara klasyczna (6 strun) − dzwieki: E2, A2
print(len(g)) #2
print()
#zad3
g1 = Gitara("Gitara klasyczna", "Strunowy", 6)
g1.dodaj_dzwiek("E2")
g1.dodaj_dzwiek("A2")
g2 = Gitara("Gitara klasyczna", "Strunowy", 6)
g2.dodaj_dzwiek("D1")
g2.dodaj_dzwiek("C2")
g3 = g1 + g2
print(g3)  # Gitara klasyczna (6 strun) − dzwieki: E2, A2, D1, C2

