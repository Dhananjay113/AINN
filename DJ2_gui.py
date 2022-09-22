print("Jai Jagannath")
from errno import ENOMSG
import tkinter as tk
from tkinter import*
from turtle import goto
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
    
    
    
    ai = 0 
    semi = 0
    eng = 0 
    dss = 0
    
    question1 = IntVar()
    question2 = IntVar()
    question3 = IntVar()
    question4 = IntVar()
    question5 = IntVar()
    
    def add_ai():
        ai = ai+1
    def add_semi():
        semi = semi+1
    def add_eng():
        eng = eng+1
    def add_dss():
       dss = dss+1
        
    q1 = Label(qframe,text="What do you think is the Technology in-demand right now :-",bg="Light Green")
    q1.place(x=10,y=100)
    q1_1 = Radiobutton(qframe,text="Ai",value=1,bg='Light Green',variable=question1,command=add_ai)
    q1_1.place(x=10,y=120)
    q1_2 = Radiobutton(qframe,text="Semiconductors",value=2,bg='Light Green',variable=question1,command=add_semi)
    q1_2.place(x=10,y=140)
    q1_3 = Radiobutton(qframe,text="Energy",value=3,bg='Light Green',variable=question1,command=add_eng)
    q1_3.place(x=10,y=160)
    q1_4 = Radiobutton(qframe,text="Data and Security",value=4,bg='Light Green',variable=question1,command=add_dss)
    q1_4.place(x=10,y=180)
    
    print(ai,dss,eng,semi)
    
    

    pokemon.destroy()


nxt_button = Button(pokemon,text="submit",command=submit)
nxt_button.pack()


    


pokemon.mainloop()
