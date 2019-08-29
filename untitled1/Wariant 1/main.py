from os.path import isfile
import tkinter as tk
from tkinter import messagebox
from PyQt5 import QtCore, QtGui, QtWidgets

import os
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
class Schronisko():

    def __init__(self, number):

        if isfile("baza") == False:
            self.number_seats = number
            self.number_animal = 0
            self.free_seats = self.number_seats
            self.animals = {}
        else:

            self.baza = self.zaladuj()
            self.number_seats = self.baza[0]
            self.number_animal = self.baza[1]
            self.free_seats = self.baza[2]
            self.animals = self.baza[3]


    def reset(self, numer_seats):
        if isfile("baza"):
            os.remove("baza")
            messagebox.showinfo("Informacja","Baza zostala Utworzona!")

        else:
            schronisko.__init__(numer_seats)
            messagebox.showinfo("Informacja","Baza zostala utworzona!")




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

    def wolne(self):
        return self.free_seats

    def remove(self, zwierze, ilosc):
        if zwierze in self.animals and self.animals[zwierze] >= ilosc:
            self.animals[zwierze] -= ilosc
            self.number_animal -= ilosc
            self.free_seats += ilosc

            if self.animals[zwierze] == 0:
                del self.animals[zwierze]


    def append(self, zwierze, ilosc):
        """
        Dodaje zwierzęta do schroniska
        :return:
        """

        #Z fukncji number_append pobiera dane

        self.number_animal += ilosc
        if zwierze in self.animals:
            self.animals[zwierze] += ilosc
        else:
            self.animals[zwierze] = ilosc

        self.free_seats -= ilosc



class Control(tk.Tk, Schronisko):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.schronisko = schronisko
        if schronisko.number_seats == None:

            self.switch_frame(PageThree)
        else:
            self.switch_frame(Framee)


    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    def Menu(self, window):

        menu = tk.Menu(self)
        nowe_cos = tk.Menu(menu)
        menu.add_cascade(label='Pliki', menu=nowe_cos)
        nowe_cos.add_command(label= 'Wieprz', command= self.wieprz(window))
        window.config(menu=menu)
    def wieprz(self, window):
        self.pobierz()
        animal_B = tk.Button(self, text="Dodaj zwierze", command = self.pobierz)
        animal_B.pack()
        remove_animal = tk.Button(self, text="Usuń zwierze", command = self.Remove_animal)
        remove_animal.pack()
        self.jakie_zwierze.pack()
        self.animals.pack()
        self.ilosc_zwierzat.pack()
        self.ilosc.pack()

    def frame(self, window):

        self.dubel = tk.Label(self, textvariable = self.text)
        self.dubel.pack()
        self.dodane = tk.StringVar()
        self.animals = tk.Entry(self, width = 10)
        self.jakie_zwierze = tk.Label(self, text = "Jakie to zwierzę?")
        self.ilosc_zwierzat = tk.Label(self, text = "Ilość zwierząt?")
        self.ilosc = tk.Spinbox(self, from_ = 0, to = 10, width= 5)

        dodane = tk.Label(self, textvariable = self.dodane)
        dodane.pack()



    def pobierz(self):

        self.a = str(self.animals.get())
        self.i = int(self.ilosc.get())
        self.free = schronisko.wolne()


        if self.i <= 0:
            self.dodane.set("Dodaj przynajmniej jedno zwierze!")
        elif self.a.isalpha() == False:
            self.dodane.set("Nazwa zwierzęcia musi się składac tylko z liter!")
        elif self.free == 0:
            self.dodane.set("Nie ma wystarczającej liczby miejsc w schronisku!")

        elif self.free > 0 and self.free < self.i:
            self.dodane.set("Nie ma wystarczającej liczby miejsc w schronisku! Dodać {} {}?".format(self.free, self.a))
            self.yorn_b = tk.Button(self, text = "Tak", command = self.yorn)
            self.yorn_b.pack(side= tk.TOP)

        else:
            schronisko.append(self.a, self.i)
            messagebox.showinfo("Informacja","Zwierze {} zostało dodane do schroniska w ilości {}".format(self.a, self.i))
        schronisko.Baza()


    def yorn(self):

        schronisko.append(self.a, self.free)
        messagebox.showinfo("Informacja","Zwierze {} zostało dodane do schroniska w ilości {}".format(self.a, self.free))
        self.yorn_b.pack_forget()
        self.dodane.set("")
        return 0

    def stan_schroniska(self):
        self.zaladuj()
        self.text.set("Witaj w schronisku! Aktualny stan schroniska:\n {}".format(self.domin))



class Framee(tk.Frame, Control, Schronisko):

    def __init__(self, window):
        tk.Frame.__init__(self, window)

        self.domin = str(schronisko)

        window.title("Schronisko")
        self.label = tk.Label( self, font = ("Times New Roman", 20),text = "Witaj w programie obsługi schroniska dla zwierząt!" )
        self.label.pack( side = tk.TOP ) # podpinanie kontrolki pod okno
        self.text = tk.StringVar()
        self.schrownisko = self.zaladuj()

        self.frame(window)

        button = tk.Button(self, text = "Sprawdz status", command = self.stan_schroniska)
        button.pack()

        tk.Button(self, text="Dodaj zwierzaka!",
                  command=lambda: window.switch_frame(PageOne)).pack()
        tk.Button(self, text="Usuń zwierzaka!",
                  command=lambda: window.switch_frame(PageTwo)).pack()

        tk.Button(self, text="Resetuj schronisko", command=lambda: window.switch_frame(PageThree)).pack()


class PageOne(tk.Frame, Control):
    def __init__(self, window):
        self.text = tk.StringVar()
        tk.Frame.__init__(self, window)
        super().frame(self)


        tk.Label(self, text="Dodawanie zwierzaka!").pack(side="top", fill="x", pady=10)

        animal_B = tk.Button(self, text="Dodaj zwierze", command=self.pobierz).pack()


        self.jakie_zwierze.pack()
        self.animals.pack()
        self.ilosc_zwierzat.pack()
        self.ilosc.pack()

        tk.Button(self, text="Return to start page",
                  command=lambda: window.switch_frame(Framee)).pack()

class PageTwo(tk.Frame, Control, Schronisko):

    def __init__(self, window):
        self.text = tk.StringVar()
        tk.Frame.__init__(self, window)
        self.animals = schronisko.animals
        self.number_animal = schronisko.number_animal
        self.free_seats = schronisko.free_seats
        labelDescription = tk.StringVar() # zminna, która będzie ustawiała tekst wypisywany w kontrolkach
        tk.Label(self, text="Usuwanie zwierzaka!").pack(side=tk.TOP, fill="x", pady=10)
        self.ct_listbox = tk.Listbox(self, width=50, height = 4)
        self.ct_listbox.pack() # wstawiam ją w oknie





        def listboxSelect(index): # to będzie funkcja, którą podepnę pod zdarzenie <<ListboxSelect>> - wywoływane, gdy zmienione zostanie zaznaczenie w kontrolce
            labelDescription.set(self.ct_listbox.get(self.ct_listbox.curselection())) # tutaj wyciągam tekst zaznaczenie i wstawiam go do zmiennej labelDescription co powoduje wyświetlenie tego tekstu w kontrolkach Entry i Label
        button = tk.Button(self, text = "Usun", command=self.buttonClicked) # tworzę przycisk, który będzie wstawiał datę
        button.pack() # wstawiam przycisk na okno główne
        for item in self.animals: # iteruję po elementach listy         s
            self.ct_listbox.insert(tk.END, item) # wstawiam je kolejno do listbox-a
            self.ct_listbox.bind('<<ListboxSelect>>', listboxSelect) # łączę zdarzenie zmiany zaznaczenia z funkcją listboxSelect

        tk.Button(self, text="Return to start page",
                  command=lambda:window.switch_frame(Framee)).pack()


    def buttonClicked(self): # zdarzenie związane z kliknięciem przycisku
        self.usuwane = self.ct_listbox.get(self.ct_listbox.curselection())

        messagebox.showinfo("Informacja","Na pewno chcesz usunac {}?".format(self.usuwane))
        self.taki = tk.Button(self, text="tak", command=self.tak)
        self.taki.pack()
    def tak(self):
        schronisko.remove(self.usuwane, 1)
        messagebox.showinfo("Informacja","Zwierze {} zostało usunięte ze schroniska!".format(self.usuwane))
        self.taki.pack_forget()

        schronisko.Baza()


class PageThree(Framee):                   
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        tk.Label(self, text="Resetowanie Schroniska").pack(side=tk.TOP, fill="x", pady=10)
        tk.Label(self, text="Podaj ilosc miejsc w schronisku").pack(side=tk.TOP, fill="x", pady=10)
        self.nowe_miejsce = tk.Entry(self, width = 10)
        self.nowe_miejsce.pack()


        button = tk.Button(self, text = "Zresetuj ilosc miejsc", command=self.pobierz_reset).pack()


        tk.Button(self, text="Return to start page",
                  command=lambda:window.switch_frame(Framee)).pack()
    def pobierz_reset(self):

        try:
            get_reset = int(self.nowe_miejsce.get())
            schronisko.reset(get_reset)
        except ValueError:
            schronisko.reset(schronisko.number_seats)


schronisko = Schronisko(None)
def closing():
    schronisko.Baza()
    app.destroy()
if __name__ == "__main__":
    app = Control()
    app.protocol("WM_DELETE_WINDOW", closing)
    app.mainloop()




