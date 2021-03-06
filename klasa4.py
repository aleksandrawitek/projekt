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
    file_path = os.path.join(base_folder, 'podstawowka.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])

def openliczbyidzialania():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'liczbyidzialania.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])

def opensystemrzymski():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'rzymskie.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])


def openpodzielnoscliczb():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'podzielnoscliczb.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])


def openfigurygeometryczne():
    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'figurygeometryczne.py')
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

tekst = Label(root, text = 'Wybierz dział:', font = "Arial 30 ", width = okno_szer, height=4,background='navajo white', fg = 'papaya whip', anchor = CENTER)
tekst.pack()

root.configure(background='papaya whip')

#dodanie przycisków oraz dopracowanie szczegółów ich wyglądu w zaleznosci od wielkosci okna

okno_dl = int(okno_dl)
okno_szer= int(okno_szer)

buttonwidth = int(0.05*okno_dl)
buttonheight = int(0.001*okno_szer)
buttonx = 0.35*okno_szer
button1y = 0.13*okno_dl
button2y = 0.17*okno_dl
button3y = 0.21*okno_dl
button4y = 0.25*okno_dl
button5y = 0.29*okno_dl


klasa4 = Button(root, text = 'Liczby i działania', width=buttonwidth, height=buttonheight, font = "Arial 20", command = openliczbyidzialania).place(x= buttonx, y=button1y)
klasa5 = Button(root, text = 'System rzymski', width=buttonwidth, height=buttonheight, font = "Arial 20", command = opensystemrzymski).place(x= buttonx, y=button2y)
klasa6 = Button(root, text = 'Figury geometryczne', width=buttonwidth, height=buttonheight, font = "Arial 20", command = openfigurygeometryczne).place(x= buttonx, y=button3y)
klasa7 = Button(root, text = 'Podzielność liczb', width=buttonwidth, height=buttonheight, font = "Arial 20", command = openpodzielnoscliczb).place(x= buttonx, y=button4y)
cofniecie = Button(root, text = 'Cofnij', width=int(0.2*buttonwidth), height=buttonheight, font = "Arial 20", command = cofnij).place(x= 0, y=0)

#dodanie zdjęcia u dołu strony dopasowanego do wymiarów okna aplikacji
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'children.png')
children = PhotoImage(file=image_path)

label = Label(image=children, width = okno_dl, height = 0.43 * okno_szer)
label.image = children
label.pack(side = BOTTOM)


root.mainloop()  