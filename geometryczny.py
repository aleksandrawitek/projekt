from tkinter import *
from PIL import Image, ImageTk
import os
from subprocess import call
from random import *



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
    file_path = os.path.join(base_folder, 'ciagi.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])

def odswiez():

    base_folder = os.path.dirname(__file__)
    file_path = os.path.join(base_folder, 'geometryczny.py')
    file_path = str(file_path)
    root.destroy()
    call(['python3', file_path])




def sprawdz():
    userinput= var.get()
    if (userinput == liczba):
        poprawna = Label(root, text = "Poprawna", background='gray79', font = "Arial 30 ", fg = 'Dark Green').place(x= 1.2*jakax, y=1.2*poly)
    else:
        blad = "Poprawny wynik - " + str(liczba)
        niepoprawna = Label(root, text = blad, background='gray79', font = "Arial 30 ", fg = 'Red2').place(x= 1.2*jakax, y=1.2*poly)


root = Tk()

#rozmiar okna, dostosowany do wymiarów ekranu uzytkownika


ekran_dl = root.winfo_screenwidth()
ekran_szer = root.winfo_screenheight()
okno_dl = 0.9*ekran_dl
okno_szer = 0.9*ekran_szer
odsx = 1.3*okno_szer
odpy = 0.25*okno_dl
odpx = 0.5*okno_szer
polex = 0.5*okno_szer
poly = 0.15*okno_dl
polx = 0.5*okno_szer
jakax = 0.8*okno_szer
sprx = 0.8*okno_szer


okno_dl = str(int(okno_dl))
okno_szer= str(int(okno_szer))
wymiar = okno_dl + 'x' + okno_szer
root.geometry(wymiar)
app = Window(root)

#dopracowanie detali wyglądu

#tekst = Label(root, text = 'Ile miejsc zerowych ma ta funkcja?', font = "Arial 30 ", width = okno_szer, height=4,background='gray63', fg = 'gray79', anchor = CENTER)
#tekst.pack()

root.configure(background='gray79')


#dodanie przycisków oraz dopracowanie szczegółów ich wyglądu w zaleznosci od wielkosci okna

okno_dl = int(okno_dl)
okno_szer= int(okno_szer)

buttonwidth = int(0.05*okno_dl)
buttonheight = int(0.001*okno_szer)




#cofniecie = Button(root, text = 'Cofnij', width=int(0.2*buttonwidth), height=buttonheight, font = "Arial 20", command = cofnij).place(x= 0, y=0)
#refresh = Button(root, text = 'Kolejny przyklad', width=int(0.35*buttonwidth), height=buttonheight, font = "Arial 20", command = odswiez).place(x= odsx, y=0)

losowanie = randrange(1,200,1)
if (losowanie <= 50):
    tekst = Label(root, text = 'Wylicz sumę n wyrazów, gdzie', font = "Arial 30 ", width = okno_szer, height=4,background='gray63', fg = 'gray79', anchor = CENTER)
    tekst.pack()
    cofniecie = Button(root, text = 'Cofnij', width=int(0.2*buttonwidth), height=buttonheight, font = "Arial 20", command = cofnij).place(x= 0, y=0)
    refresh = Button(root, text = 'Kolejny przyklad', width=int(0.35*buttonwidth), height=buttonheight, font = "Arial 20", command = odswiez).place(x= odsx, y=0)
    a = randrange(-30,30,1)
    b = randrange(-20,20,1)
    n = randrange(1,10,1)

    if (b == 1):
        liczba = n*a
    else:
        liczba = a *(1 - (b**n))/(1-b)


    if (a < 0):
        a = '(' + str(a) + ')'
    if (b < 0):
        b = '(' + str(b) + ')'
   

    poleconko = 'a1 = ' + str(a) + ', q = ' + str(b) + ', n = ' + str(n) 


elif (losowanie > 50 and losowanie <= 100):
    tekst = Label(root, text = 'Wylicz n-ty wyraz, gdzie', font = "Arial 30 ", width = okno_szer, height=4,background='gray63', fg = 'gray79', anchor = CENTER)
    tekst.pack()
    cofniecie = Button(root, text = 'Cofnij', width=int(0.2*buttonwidth), height=buttonheight, font = "Arial 20", command = cofnij).place(x= 0, y=0)
    refresh = Button(root, text = 'Kolejny przyklad', width=int(0.35*buttonwidth), height=buttonheight, font = "Arial 20", command = odswiez).place(x= odsx, y=0)
    a = randrange(-30,30,1)
    b = randrange(-20,20,1)
    n = randrange(1,5,1)

    liczba = a*(b**(n-1))


    if (a < 0):
        a = '(' + str(a) + ')'
    if (b < 0):
        b = '(' + str(b) + ')'
   

    poleconko = 'a1 = ' + str(a) + ', q = ' + str(b) + ', n = ' + str(n) 

elif (losowanie > 100 and losowanie <= 150):
    tekst = Label(root, text = 'Wylicz iloraz ciagu, gdzie', font = "Arial 30 ", width = okno_szer, height=4,background='gray63', fg = 'gray79', anchor = CENTER)
    tekst.pack()
    cofniecie = Button(root, text = 'Cofnij', width=int(0.2*buttonwidth), height=buttonheight, font = "Arial 20", command = cofnij).place(x= 0, y=0)
    refresh = Button(root, text = 'Kolejny przyklad', width=int(0.35*buttonwidth), height=buttonheight, font = "Arial 20", command = odswiez).place(x= odsx, y=0)
    a = randrange(-30,30,1)
    b = randrange(-20,20,1)
    n = randrange(1,5,1)

    liczba = int(b)

    an = a*(b**(n-1))


    if (a < 0):
        a = '(' + str(a) + ')'
    if (b < 0):
        b = '(' + str(b) + ')'
    if (an < 0):
        an = '(' + str(an) + ')'
   

    poleconko = 'a1 = ' + str(a) + ', an = ' + str(an) + ', n = ' + str(n) 
else:
    tekst = Label(root, text = 'Wylicz pierszy wyraz ciagu, gdzie', font = "Arial 30 ", width = okno_szer, height=4,background='gray63', fg = 'gray79', anchor = CENTER)
    tekst.pack()
    cofniecie = Button(root, text = 'Cofnij', width=int(0.2*buttonwidth), height=buttonheight, font = "Arial 20", command = cofnij).place(x= 0, y=0)
    refresh = Button(root, text = 'Kolejny przyklad', width=int(0.35*buttonwidth), height=buttonheight, font = "Arial 20", command = odswiez).place(x= odsx, y=0)
    a = randrange(-30,30,1)
    b = randrange(-20,20,1)
    n = randrange(1,5,1)

    liczba = int(a)

    an = a*(b**(n-1))


    if (a < 0):
        a = '(' + str(a) + ')'
    if (b < 0):
        b = '(' + str(b) + ')'
    if (an < 0):
        an = '(' + str(an) + ')'
   

    poleconko = 'q = ' + str(b) + ', an = ' + str(an) + ', n = ' + str(n) 

polecenie = Label(root, text = poleconko, background='gray79', font = "Arial 30 ", fg = 'black').place(x= polx, y=poly)



var = IntVar()
odpowiedz = Label(root, text = "Odpowiedz", background='gray79', font = "Arial 30 ", fg = 'black').place(x= odpx, y=odpy)
poletekstowe = Entry(root, bd = 10, textvariable=var).place(x= polex, y=odpy)

sprawdzenie = Button(root, text = 'Enter', width=int(0.2*buttonwidth), height=buttonheight, font = "Arial 20", command = sprawdz).place(x= sprx, y=odpy)



#dodanie zdjęcia u dołu strony dopasowanego do wymiarów okna aplikacji
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'owl.png')
owl = PhotoImage(file=image_path)

label = Label(image=owl, width = okno_dl, height = 0.43 * okno_szer)
label.image = owl
label.pack(side = BOTTOM)



root.mainloop()  