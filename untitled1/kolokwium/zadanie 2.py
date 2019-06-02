class Zapiekanka():
    def __init__(self, dlugosc, kcal, cena):
        self.dlugosc = dlugosc
        self.kcal = kcal
        self.cena_za_cm = cena
        self.nazwa = ""


    @property
    def Koszt(self):
        koszt = self.dlugosc * self.cena_za_cm
        return koszt

    def __str__(self):
        tekst = "Zapiekanka {} ma {} m dlugosci, {} kalorii a jej koszt wynosi {}"
        return str("Zapiekanka {} ma {} m dlugosci, {} kalorii a jej koszt wynosi {} ".format(self.nazwa, self.dlugosc, self.kcal, self.Koszt))

    def __repr__(self):
        return "To jest obiekt klasy zapiekanka"

    def __add__(self, other):
        dlugosc = self.dlugosc + other.dlugosc
        kcal = self.kcal + other.kcal
        nowa_zapiekanka = self.cena_za_cm * self.dlugosc/dlugosc + self.cena_za_cm * other.dlugosc/dlugosc
        return Zapiekanka(dlugosc, kcal, nowa_zapiekanka)

zapiekanka = Zapiekanka(12, 23, 10)
zapiekanka2 = Zapiekanka(14, 300, 12)

zapiekanka3 = zapiekanka + zapiekanka2


print(zapiekanka)
print(zapiekanka.Koszt)
print(zapiekanka3)


