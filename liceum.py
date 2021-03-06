from tkinter import *
from PIL import Image, ImageTk
import os
from subprocess import call

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #stworzenie nowego okna
    def init_window(self):

        #nadanie tytułu      
        self.master.title("Platforma Edukacyjna")

def cofnij():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'startowa.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])

def openliczby():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'liczby.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])


def openfunkcje():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'funkcje.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])

def openciagi():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'ciagi.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])

def opentrygo():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'trygonometria.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])


root = Tk()

#rozmiar okna, dostosowany do wymiarów ekranu uzytkownika

ekran_dl = root.winfo_screenwidth()
ekran_szer = root.winfo_screenheight()
okno_dl = 0.9*ekran_dl
okno_szer = 0.9*ekran_szer
okno_dl = str(int(okno_dl))
okno_szer= str(int(okno_szer))
wymiar = okno_dl + 'x' + okno_szer
root.geometry(wymiar)
app = Window(root)

#dopracowanie detali wyglądu

tekst = Label(root, text = 'Wybierz dział:', font = "Arial 30 ", width = okno_szer, height=4,background='gray63', fg = 'gray79', anchor = CENTER)
tekst.pack()

root.configure(background='gray79')

#dodanie przycisków oraz dopracowanie szczegółów ich wyglądu w zaleznosci od wielkosci okna

okno_dl = int(okno_dl)
okno_szer= int(okno_szer)

buttonwidth = int(0.05*okno_dl)
buttonheight = int(0.001*okno_szer)
buttonx = 0.35*okno_szer
button1y = 0.15*okno_dl
button2y = 0.19*okno_dl
button3y = 0.23*okno_dl
button4y = 0.27*okno_dl
button5y = 0.31*okno_dl


klasa1 = Button(root, text = 'Liczby', width=buttonwidth, height=buttonheight, font = "Arial 20", command = openliczby).place(x= buttonx, y=button1y)
klasa2 = Button(root, text = 'Funkcje', width=buttonwidth, height=buttonheight, font = "Arial 20", command = openfunkcje).place(x= buttonx, y=button2y)
klasa3 = Button(root, text = 'Ciągi', width=buttonwidth, height=buttonheight, font = "Arial 20", command = openciagi).place(x= buttonx, y=button3y)
klasa4 = Button(root, text = 'Trygonometria', width=buttonwidth, height=buttonheight, font = "Arial 20", command = opentrygo).place(x= buttonx, y=button4y)
cofniecie = Button(root, text = 'Cofnij', width=int(0.2*buttonwidth), height=buttonheight, font = "Arial 20", command = cofnij).place(x= 0, y=0)


#dodanie zdjęcia u dołu strony dopasowanego do wymiarów okna aplikacji
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'owl.png')
owl = PhotoImage(file=image_path)

label = Label(image=owl, width = okno_dl, height = 0.43 * okno_szer)
label.image = owl
label.pack(side = BOTTOM)


root.mainloop()  