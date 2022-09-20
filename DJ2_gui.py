print("Jai Jagannath")
import tkinter as tk
from tkinter import*
#import tkinter as Tk

pokemon = Tk()
pokemon.geometry("500x500")
#pokemon.configure(bg="Light Blue")

'''
q_frame = Frame(pokemon)
q_frame.pack()
'''

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

    qframe_headding = Label(qframe,text="Question Time",bg='Light Green',font=("Helvetica", 16))
    qframe_headding.pack()
    
    space = Label(qframe, text=" ",bg="Light Green",font=("Helvetica", 20))
    space.pack()
    
    qframe_subheadding = Label(qframe,text="Please answer the following questions:-",bg='Light Green',font=("Helvetica", 10))
    qframe_subheadding.pack()
    
    
    q1 = Label(qframe,text="What do you think is the Technology in-demand right now :-",bg="Light Green")
    q1.pack()
    
   

    pokemon.destroy()


nxt_button = Button(pokemon,text="submit",command=submit)
nxt_button.pack()




pokemon.mainloop()
