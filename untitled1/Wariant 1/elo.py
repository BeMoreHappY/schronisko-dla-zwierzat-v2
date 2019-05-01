from os.path import isfile
import tkinter as tk
import time
class Schronisko():

    def __init__(self):

        if isfile("baza") == False:
            self.number_seats = int(input("Podaj ilosc miejsc w schronisku: "))
            self.number_animal = 0
            self.free_seats = self.number_seats
            self.animals = {}
        else:

            self.baza = self.zaladuj()
            self.number_seats = self.baza[0]
            self.number_animal = self.baza[1]
            self.free_seats = self.baza[2]
            self.animals = self.baza[3]


    def zaladuj(self):
        import pickle
        self.baza = []
        try:
            with open("baza", "rb") as f:
                self.baza = pickle.load(f)
        except FileNotFoundError:
            pass
        return self.baza

    def Baza(self):
        import pickle

        with open("baza", "wb") as f:
            dane = [self.number_seats, self.number_animal, self.free_seats, self.animals]
            pickle.dump(dane, f)



    def __str__(self):
        """
        Wyświetla aktualny stan schroniska
        :return:
        """
        liczba_zwierzat = "Liczba zwierząt: {}".format(self.number_animal)
        liczba_miejsc = "Liczba wolnych miejsc: {}".format(self.free_seats)
        Zwierzeta = "Zwierzęta w schronisku: {}".format(self.animals)
        return liczba_zwierzat + '\n' + liczba_miejsc + '\n' + Zwierzeta



    def append(self, zwierze1, ilosc):
        """
        Dodaje zwierzęta do schroniska
        :return:
        """
        if self.free_seats == 0:                                        #Sprawdza czy jest miejsce w schronisku
            return False
        zwierze = [zwierze1, ilosc]
                                         #Z fukncji number_append pobiera dane
        print("elo")
        if zwierze[1] > self.free_seats:
            return 2, self.free_seats
        else:
            self.number_animal += zwierze[1]
            if zwierze[0] in self.animals:
                self.animals[zwierze[0]] += zwierze[1]
            else:
                self.animals[zwierze[0]] = zwierze[1]

            self.free_seats -= zwierze[1]
            print("Zwierze zostało dodane!")
        return "elo", "melo"







class Framee():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Schronisko")
        self.text = tk.StringVar()
        self.schronisko = Schronisko()
        self.domin = self.schronisko
        self.frame()


    def frame(self):
        self.label = tk.Label( self.window, font = ("Times New Roman", 20),text = "Witaj w programie obsługi schroniska dla zwierząt!" )
        self.label.pack( side = tk.TOP ) # podpinanie kontrolki pod okno
        self.dubel = tk.Label(self.window, textvariable = self.text)
        self.dubel.pack()
        self.dodane = tk.StringVar()

        jakie_zwierze = tk.Label(self.window, text = "Jakie to zwierzę?")
        jakie_zwierze.pack()

        self.animals = tk.Entry(self.window, width = 10)
        self.animals.pack()

        ilosc_zwierzat = tk.Label(self.window, text = "Ilość zwierząt?")
        ilosc_zwierzat.pack()
        self.ilosc = tk.Spinbox(self.window, from_ = 0, to = 10)
        self.ilosc.pack()

        dodane = tk.Label(self.window, textvariable = self.dodane)
        dodane.pack()
        print("pobierz")
        animal_B = tk.Button(self.window, text="Dodaj zwierze", command=self.pobierz)
        animal_B.pack()
        button = tk.Button(self.window, text = "Aktualizuj", command = self.stan_schroniska)
        button.pack()

    def pobierz(self):
        self.a = str(self.animals.get())
        self.i = int(self.ilosc.get())

        print("pobierz1")
        if self.i <= 0:
            self.dodane.set("Dodaj przynajmniej jedno zwierze!")
        elif self.a.isalpha() == False:
            self.dodane.set("Nazwa zwierzęcia nie skłąda się z cyfr!")
        elif self.schronisko.append(self.a, self.i) == False:
            self.dodane.set("Nie ma wystarczającej liczby miejsc w schronisku!")

        elif self.schronisko.append(self.a, self.i)[0] == 2:
            print("elif")
            self.free =  self.schronisko.append(self.a, self.i)[1]
            self.dodane.set("Nie ma wystarczającej liczby miejsc w schronisku! Dodać {} {}?".format(self.schronisko.append(self.a, self.i)[1], self.a))
            self.yorn_b = tk.Button(self.window, text = "Tak", command = self.yorn)
            self.yorn_b.pack()

        else:
            print("else")
            self.schronisko.append(self.a, self.i)
            self.dodane.set("Zwierze {} zostało dodane do schroniska w ilości {}".format(self.a, self.i))


    def yorn(self):
        self.schronisko.append(self.a, self.schronisko.append(self.a, self.free))
        self.yorn_b.pack_forget()
        self.dodane.set("")
        return 0

    def stan_schroniska(self):
        self.text.set("Witaj w schronisku! Aktualny stan schroniska:\n {}".format(self.domin))




window = Framee()


tk.mainloop()