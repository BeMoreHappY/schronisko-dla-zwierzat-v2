class Schronisko():

    def __init__(self, number_seats):
        self.number_seats = number_seats
        self.number_animal = 0
        self.free_seats = number_seats - self.number_animal
        self.animals = {}

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
        animal = input("Jakie to zwierze: ").lower()
        ilosc = int(input("Podaj ilosc: "))
        return animal, ilosc

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



schronisko = Schronisko(20)

print(schronisko)

schronisko.append()

print(schronisko)

