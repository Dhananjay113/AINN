print("Jai Jagannath")

import tkinter as tk
from tkinter import*

pokemon = Tk()
pokemon.geometry("1000x1000")
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


ai = 0
semi = 0
eng = 0
dss = 0


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
    
    
    
    
    
    question1 = IntVar()
    question2 = IntVar()
    question3 = IntVar()
    question4 = IntVar()
    question5 = IntVar()
    
    def add_ai():
        global ai
        ai = ai+1
        print(ai)
    def add_semi():
        global semi
        semi = semi+1
        print(semi)
    def add_eng():
        global eng
        eng = eng+1
        print(eng)
    def add_dss():
        global dss
        dss = dss+1
        print(dss)
        
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
    
    
    q2 = Label(qframe,text="What do you think the government ahould invest on if it had 10 billion doller :-",bg="Light Green")
    q2.place(x=10,y=200)
    q2_1 = Radiobutton(qframe,text="Improve our military",value=5,bg='Light Green',variable=question2,command=add_dss)
    q2_1.place(x=10,y=220)
    q2_2 = Radiobutton(qframe,text="Do something to improve the income",value=6,bg='Light Green',variable=question2,command=add_eng)
    q2_2.place(x=10,y=240)
    q2_3 = Radiobutton(qframe,text="Invest in manufacturing",value=7,bg='Light Green',variable=question2,command=add_semi)
    q2_3.place(x=10,y=260)
    q2_4 = Radiobutton(qframe,text="have it as a back up",value=8,bg='Light Green',variable=question2,command=add_ai)
    q2_4.place(x=10,y=280)
    
    
    q3 = Label(qframe,text="Who do you like in thi list :-",bg="Light Green")
    q3.place(x=10,y=300)
    q3_1 = Radiobutton(qframe,text="Iscac Newton",value=5,bg='Light Green',variable=question3,command=add_ai)
    q3_1.place(x=10,y=320)
    q3_2 = Radiobutton(qframe,text="Gausess",value=6,bg='Light Green',variable=question3,command=add_eng)
    q3_2.place(x=10,y=340)
    q3_3 = Radiobutton(qframe,text="Ted Hoff",value=7,bg='Light Green',variable=question3,command=add_semi)
    q3_3.place(x=10,y=360)
    q3_4 = Radiobutton(qframe,text="Satoshi Nakamoto",value=8,bg='Light Green',variable=question3,command=add_ai)
    q3_4.place(x=10,y=380)
    
    q4 = Label(qframe,text="Which of these companies do you like in this list :-",bg="Light Green")
    q4.place(x=10,y=400)
    q4_1 = Radiobutton(qframe,text="Google",value=5,bg='Light Green',variable=question4,command=add_ai)
    q4_1.place(x=10,y=420)
    q4_2 = Radiobutton(qframe,text="Tesla",value=6,bg='Light Green',variable=question4,command=add_eng)
    q4_2.place(x=10,y=440)
    q4_3 = Radiobutton(qframe,text="Intel",value=7,bg='Light Green',variable=question4,command=add_semi)
    q4_3.place(x=10,y=460)
    q4_4 = Radiobutton(qframe,text="IBM",value=8,bg='Light Green',variable=question4,command=add_ai)
    q4_4.place(x=10,y=480)
   
    q5 = Label(qframe,text="what would you do from the given options in your freetime :-",bg="Light Green")
    q5.place(x=10,y=500)
    q5_1 = Radiobutton(qframe,text="Cycle",value=5,bg='Light Green',variable=question5,command=add_eng)
    q5_1.place(x=10,y=520)
    q5_2 = Radiobutton(qframe,text="Code",value=6,bg='Light Green',variable=question5,command=add_ai)
    q5_2.place(x=10,y=540)
    q5_3 = Radiobutton(qframe,text="Play with PCBs",value=7,bg='Light Green',variable=question5,command=add_semi)
    q5_3.place(x=10,y=560)
    q5_4 = Radiobutton(qframe,text="Scout",value=8,bg='Light Green',variable=question5,command=add_dss)
    q5_4.place(x=10,y=580)
    
    
    def pikachu():
        global ai
        global semi
        global eng
        global dss
        if(ai>semi and ai>eng and ai>dss ):
            mitemasu = open(r'C:\Users\student\Desktop\TOP SECRET\ai.txt', 'r')
            print(mitemasu.read())
            mitemasu.close()
        elif (semi>ai and semi>eng and semi>dss ):
            mitemasu = open(r'C:\Users\student\Desktop\TOP SECRET\semi.txt', 'r')    
            print(mitemasu.read())
            mitemasu.close()
        elif (eng>ai and eng>semi and eng>dss ):
            mitemasu = open(r'C:\Users\student\Desktop\TOP SECRET\eng.txt', 'r')
            print(mitemasu.read())
            mitemasu.close()
        elif (dss>ai and dss>semi and dss>eng):
            mitemasu = open(r'C:\Users\student\Desktop\TOP SECRET\dss.txt', 'r')
            print(mitemasu.read())
            mitemasu.close()
            
   
    pikachu_button = Button(qframe,text="Submit",command=pikachu)
    pikachu_button.place(x=50,y=600)

    pokemon.destroy()


nxt_button = Button(pokemon,text="submit",command=submit)
nxt_button.pack()


    


pokemon.mainloop()
