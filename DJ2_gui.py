print("Jai Jagannath")
import tkinter as tk
from tkinter import*
#import tkinter as Tk

pokemon = Tk()
pokemon.geometry("500x500")
#pokemon.configure(bg="Light Blue")


pokemon.title("DJ's Course Recomendation System Ultra Pro Max")
headding=Label(pokemon, text="Welcome Kodomo!", font=("Helvetica", 16))
headding.pack()

space = Label(pokemon, text=" ",font=("Helvetica", 20))
space.pack()

name_lable = Label(pokemon, text="Kodomo no namae:-",font=("Helvetica", 10))
name_lable.pack()
name = Entry(pokemon)
name.pack()

degree_lable = Label(pokemon, text="Kodomo no namae:-",font=("Helvetica", 10))
degree_lable.pack()
degree = Entry(pokemon)
degree.pack()



def submit():
    qframe = Tk()
    qframe.geometry("500x500")
    qframe.configure(bg="Light Green")
    print(name.get(),degree.get())

    qframe.title("Question Time")

    lable = Label(qframe,text="Question Time",bg='Green')
    lable.pack()

    pokemon.destroy()


nxt_button = Button(pokemon,text="submit",command=submit)
nxt_button.pack()




pokemon.mainloop()
