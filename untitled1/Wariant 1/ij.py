import tkinter as tk # ładowanie modułu tkinter (w wersji 3+)

window = tk.Tk() # tworzenie okna głównego
window.title( "Hello World" ) # ustawienie tytułu okna głównego
# tworzenie kontrolki typu label
text = tk.StringVar()
label = tk.Label( window, textvariable = text, padx=100, pady=20)
label.pack() # podpinanie kontrolki pod okno
text.set("Witaj Świecie programowania\nCo swym urokiem nas zabawia\nCo otwiera nowe możliwości\nZ binarnych liczb złożoności")
description = tk.Label(window, text="Podaj proszę swoje imie:").pack()
name = tk.Entry(window,width=40)
name.pack()
def HelloWorld():
    text.set("Witaj {0} w świecie programowania\nCo swym urokiem nas zabawia\nCo otwiera nowe możliwości\nZ binarnych liczb złożoności".format(name.get()))
ok = tk.Button(window, text="OK", width=20, command=HelloWorld)
ok.pack()

tk.mainloop() # wywołanie pętli komunikatów