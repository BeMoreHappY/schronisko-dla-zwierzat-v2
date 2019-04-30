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

    def number_append(self):
        """
        Pobiera liczbe zwierząt do dodania
        :return:
        """


        a = gad
        b = wartosc

        return a, b

    def append(self):
        """
        Dodaje zwierzęta do schroniska
        :return:
        """
        if self.free_seats == 0:                                        #Sprawdza czy jest miejsce w schronisku
            return print("Zbyt mało miejsca w schroniku")

        zwierze = self.number_append()                                  #Z fukncji number_append pobiera dane

        if zwierze[1] > self.free_seats:
            print("Nie ma wystarczającej liczby miejsc")
            print("Dodać {} {}?" .format(self.free_seats, zwierze[0]))
            if input("Y or N?").lower() == "y":
                self.number_animal += self.free_seats
                if zwierze[0] in self.animals:
                    self.animals[zwierze[0]] += self.free_seats
                else:
                    self.animals[zwierze[0]] = self.free_seats

                self.free_seats = 0
        else:
            self.number_animal += zwierze[1]
            if zwierze[0] in self.animals:
                self.animals[zwierze[0]] += zwierze[1]
            else:
                self.animals[zwierze[0]] = zwierze[1]

            self.free_seats -= zwierze[1]
            print("Zwierze zostało dodane!")





class Frame():

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
        button = tk.Button(self.window, text = "Aktualizuj", command = self.stan_schroniska)
        button.pack()
        button2 = tk.Button(self.window, text = "Dodaj zwierzaka", command = self.schronisko.append)
        button2.pack()
        global gad
        global wartosc
        self.animal = tk.Entry(self.window, width = 40)
        self.animal.pack()
        self.value = tk.IntVar()
        spinbox = tk.Spinbox(self.window, from_ = 3, to = 10, textvariable = self.value)
        spinbox.pack()
        gad = self.animal.get()
        wartosc = self.value.get()



    def stan_schroniska(self):
        self.text.set("Witaj w schronisku! Aktualny stan schroniska:\n {}".format(self.domin))













window = Frame()


tk.mainloop()