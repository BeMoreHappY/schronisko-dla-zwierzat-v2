from os.path import isfile
import tkinter as tk
from tkinter import messagebox
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
        print("Zwierze zostało dodane!")


class Control(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Framee)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(Framee)).pack()

class Framee(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.window = tk.Tk()
        self.window.title("Schronisko")
        self.text = tk.StringVar()
        self.schronisko = Schronisko()
        self.domin = self.schronisko
        self.frame()
        self.schronisko.zaladuj()
        self.Menu()

        tk.Button(self, text="Open page one",
                  command=lambda: master.switch_frame(PageOne)).pack()

    def Menu(self):
        menu = tk.Menu(self.window)
        nowe_cos = tk.Menu(menu)
        menu.add_cascade(label='Pliki', menu=nowe_cos)
        nowe_cos.add_command(label= 'Wieprz', command= self.wieprz)
        self.window.config(menu=menu)
    def wieprz(self):
        self.pobierz()
        animal_B = tk.Button(self.window, text="Dodaj zwierze", command = self.pobierz)
        animal_B.pack()
        remove_animal = tk.Button(self.window, text="Usuń zwierze", command = self.Remove_animal)
        remove_animal.pack()
        self.jakie_zwierze.pack()
        self.animals.pack()
        self.ilosc_zwierzat.pack()
        self.ilosc.pack()

    def frame(self):
        self.label = tk.Label( self.window, font = ("Times New Roman", 20),text = "Witaj w programie obsługi schroniska dla zwierząt!" )
        self.label.pack( side = tk.TOP ) # podpinanie kontrolki pod okno
        self.dubel = tk.Label(self.window, textvariable = self.text)
        self.dubel.pack()
        self.dodane = tk.StringVar()
        self.animals = tk.Entry(self.window, width = 10)
        self.jakie_zwierze = tk.Label(self.window, text = "Jakie to zwierzę?")
        self.ilosc_zwierzat = tk.Label(self.window, text = "Ilość zwierząt?")
        self.ilosc = tk.Spinbox(self.window, from_ = 0, to = 10, width= 5)

        dodane = tk.Label(self.window, textvariable = self.dodane)
        dodane.pack()

        button = tk.Button(self.window, text = "Sprawdz status", command = self.stan_schroniska)
        button.pack()

    def pobierz(self):

        self.a = str(self.animals.get())
        self.i = int(self.ilosc.get())
        self.free = self.schronisko.wolne()


        if self.i <= 0:
            self.dodane.set("Dodaj przynajmniej jedno zwierze!")
        elif self.a.isalpha() == False:
            self.dodane.set("Nazwa zwierzęcia musi się składac tylko z liter!")
        elif self.free == 0:
            self.dodane.set("Nie ma wystarczającej liczby miejsc w schronisku!")

        elif self.free > 0 and self.free < self.i:
            self.dodane.set("Nie ma wystarczającej liczby miejsc w schronisku! Dodać {} {}?".format(self.free, self.a))
            self.yorn_b = tk.Button(self.window, text = "Tak", command = self.yorn)
            self.yorn_b.pack(side= tk.TOP)

        else:
            self.schronisko.append(self.a, self.i)
            messagebox.showinfo("Informacja","Zwierze {} zostało dodane do schroniska w ilości {}".format(self.a, self.i))
        self.schronisko.Baza()


    def Remove_animal(self):
        self.animals.pack_forget()
        self.jakie_zwierze.pack_forget()
        self.ilosc_zwierzat.pack_forget()
        self.ilosc.pack_forget()

        self.jakie_zwierze.pack()

        self.animals.pack_forget()
        self.animals.pack()



        self.ilosc_zwierzat.pack()

        self.ilosc.pack()

        self.a = str(self.animals.get())
        self.i = int(self.ilosc.get())

        if self.i > 0:
            self.schronisko.remove(self.a, self.i)
            messagebox.showinfo("Informacja","Zwierze {} zostało usunięte ze schroniska!".format(self.a))
        else:
            messagebox.showinfo("Informacja","Ile zwierząt usunąć?")


    def yorn(self):

        self.schronisko.append(self.a, self.free)
        self.yorn_b.pack_forget()
        self.dodane.set("")
        return 0

    def stan_schroniska(self):
        self.text.set("Witaj w schronisku! Aktualny stan schroniska:\n {}".format(self.domin))



if __name__ == "__main__":
    app = Control()
    app.mainloop()