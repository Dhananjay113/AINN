print("Jai Jagannath")

import tkinter as tk
from tkinter import*
import webbrowser


pokemon = Tk()
pokemon.geometry("1000x1000")

pokemon.title("DJ's Course Recomendation System Pro Max Ultima")
headding=Label(pokemon, text="Welcome Student!", font=("Helvetica", 16))
headding.pack()

space = Label(pokemon, text=" ",font=("Helvetica", 20))
space.pack()

name_lable = Label(pokemon, text="Student Name:-",font=("Helvetica", 10))
name_lable.pack()
name = Entry(pokemon)
name.pack()

degree_lable = Label(pokemon, text="Department:-",font=("Helvetica", 10))
degree_lable.pack()
degree = Entry(pokemon)
degree.pack()


ai = 0
semi = 0
eng = 0
dss = 0


def rotom():
    pikachu = Tk()
    pikachu.geometry("750x750")
    pikachu.configure(bg="Light Green")
    print(name.get(),degree.get())

    pikachu.title("Question Time")
    
    pikachu_headding = Label(pikachu,text="Question Time",bg='Light Green',font=("Helvetica", 16))
    pikachu_headding.pack()
    
    space = Label(pikachu, text=" ",bg="Light Green",font=("Helvetica", 20))
    space.pack()
    
    pikachu_subheadding = Label(pikachu,text="Please answer the following questions:-",bg='Light Green',font=("Helvetica", 10))
    pikachu_subheadding.pack()
    
    
    
    
    
    question1 = IntVar()
    question2 = IntVar()
    question3 = IntVar()
    question4 = IntVar()
    question5 = IntVar()
    question6 = IntVar()
    question7 = IntVar()
    question8 = IntVar()
    
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
        
    q1 = Label(pikachu,text="What do you think is the Technology in-demand right now :-",bg="Light Green")
    q1.place(x=10,y=100)
    q1_1 = Radiobutton(pikachu,text="Ai",value=1,bg='Light Green',variable=question1,command=add_ai)
    q1_1.place(x=10,y=120)
    q1_2 = Radiobutton(pikachu,text="Semiconductors",value=2,bg='Light Green',variable=question1,command=add_semi)
    q1_2.place(x=10,y=140)
    q1_3 = Radiobutton(pikachu,text="Energy",value=3,bg='Light Green',variable=question1,command=add_eng)
    q1_3.place(x=10,y=160)
    q1_4 = Radiobutton(pikachu,text="Data and Security",value=4,bg='Light Green',variable=question1,command=add_dss)
    q1_4.place(x=10,y=180)
    
    
    q2 = Label(pikachu,text="What do you think the government ahould invest on if it had 10 billion doller :-",bg="Light Green")
    q2.place(x=10,y=200)
    q2_1 = Radiobutton(pikachu,text="Improve our military",value=5,bg='Light Green',variable=question2,command=add_dss)
    q2_1.place(x=10,y=220)
    q2_2 = Radiobutton(pikachu,text="Do something to improve the income",value=6,bg='Light Green',variable=question2,command=add_eng)
    q2_2.place(x=10,y=240)
    q2_3 = Radiobutton(pikachu,text="Invest in manufacturing",value=7,bg='Light Green',variable=question2,command=add_semi)
    q2_3.place(x=10,y=260)
    q2_4 = Radiobutton(pikachu,text="have it as a back up",value=8,bg='Light Green',variable=question2,command=add_ai)
    q2_4.place(x=10,y=280)
    
    
    q3 = Label(pikachu,text="Who do you like in thi list :-",bg="Light Green")
    q3.place(x=10,y=300)
    q3_1 = Radiobutton(pikachu,text="Iscac Newton",value=5,bg='Light Green',variable=question3,command=add_ai)
    q3_1.place(x=10,y=320)
    q3_2 = Radiobutton(pikachu,text="Gausess",value=6,bg='Light Green',variable=question3,command=add_eng)
    q3_2.place(x=10,y=340)
    q3_3 = Radiobutton(pikachu,text="Ted Hoff",value=7,bg='Light Green',variable=question3,command=add_semi)
    q3_3.place(x=10,y=360)
    q3_4 = Radiobutton(pikachu,text="Satoshi Nakamoto",value=8,bg='Light Green',variable=question3,command=add_ai)
    q3_4.place(x=10,y=380)
    
    q4 = Label(pikachu,text="Which of these companies do you like in this list :-",bg="Light Green")
    q4.place(x=10,y=400)
    q4_1 = Radiobutton(pikachu,text="Google",value=5,bg='Light Green',variable=question4,command=add_ai)
    q4_1.place(x=10,y=420)
    q4_2 = Radiobutton(pikachu,text="Tesla",value=6,bg='Light Green',variable=question4,command=add_eng)
    q4_2.place(x=10,y=440)
    q4_3 = Radiobutton(pikachu,text="Intel",value=7,bg='Light Green',variable=question4,command=add_semi)
    q4_3.place(x=10,y=460)
    q4_4 = Radiobutton(pikachu,text="IBM",value=8,bg='Light Green',variable=question4,command=add_ai)
    q4_4.place(x=10,y=480)
   
    q5 = Label(pikachu,text="what would you do from the given options in your freetime :-",bg="Light Green")
    q5.place(x=10,y=500)
    q5_1 = Radiobutton(pikachu,text="Cycle",value=5,bg='Light Green',variable=question5,command=add_eng)
    q5_1.place(x=10,y=520)
    q5_2 = Radiobutton(pikachu,text="Code",value=6,bg='Light Green',variable=question5,command=add_ai)
    q5_2.place(x=10,y=540)
    q5_3 = Radiobutton(pikachu,text="Play with PCBs",value=7,bg='Light Green',variable=question5,command=add_semi)
    q5_3.place(x=10,y=560)
    q5_4 = Radiobutton(pikachu,text="Scout",value=8,bg='Light Green',variable=question5,command=add_dss)
    q5_4.place(x=10,y=580)
    
    q6 = Label(pikachu,text="what do you think from the following is great for our nation :-",bg="Light Green")
    q6.place(x=400,y=100)
    q6_1 = Radiobutton(pikachu,text="Strong Military",value=5,bg='Light Green',variable=question6,command=add_dss)
    q6_1.place(x=400,y=120)
    q6_2 = Radiobutton(pikachu,text="Independance from resource dependance",value=6,bg='Light Green',variable=question6,command=add_eng)
    q6_2.place(x=400,y=140)
    q6_3 = Radiobutton(pikachu,text="Recreate TSMC",value=7,bg='Light Green',variable=question6,command=add_semi)
    q6_3.place(x=400,y=160)
    q6_4 = Radiobutton(pikachu,text="Cyber supremacy",value=8,bg='Light Green',variable=question6,command=add_ai)
    q6_4.place(x=400,y=180)
    
    q7 = Label(pikachu,text="which the following fascinates you :-",bg="Light Green")
    q7.place(x=400,y=220)
    q7_1 = Radiobutton(pikachu,text="Aluminium",value=5,bg='Light Green',variable=question7,command=add_eng)
    q7_1.place(x=400,y=240)
    q7_2 = Radiobutton(pikachu,text="TRADIC ",value=6,bg='Light Green',variable=question7,command=add_semi)
    q7_2.place(x=400,y=260)
    q7_3 = Radiobutton(pikachu,text="Google Assistant",value=7,bg='Light Green',variable=question7,command=add_semi)
    q7_3.place(x=400,y=280)
    q7_4 = Radiobutton(pikachu,text="Cloud",value=8,bg='Light Green',variable=question7,command=add_dss)
    q7_4.place(x=400,y=300)
    
    q8 = Label(pikachu,text="What movie you like :-",bg="Light Green")
    q8.place(x=400,y=320)
    q8_1 = Radiobutton(pikachu,text="Mortal Engins",value=5,bg='Light Green',variable=question8,command=add_eng)
    q8_1.place(x=400,y=340)
    q8_2 = Radiobutton(pikachu,text="MAtrix",value=6,bg='Light Green',variable=question8,command=add_dss)
    q8_2.place(x=400,y=360)
    q8_3 = Radiobutton(pikachu,text="G.I Joe",value=7,bg='Light Green',variable=question8,command=add_semi)
    q8_3.place(x=400,y=380)
    q8_4 = Radiobutton(pikachu,text="IROBO",value=8,bg='Light Green',variable=question8,command=add_ai)
    q8_4.place(x=400,y=400)
    
    
    def palkiya():
        global ai
        global semi
        global eng
        global dss
        
        def ai_():
            webbrowser.open('https://raw.githubusercontent.com/Dhananjay113/AINN/main/ai.txt')  # Go to example.com
        def semi_():
            webbrowser.open('https://raw.githubusercontent.com/Dhananjay113/AINN/main/Embedded_systems.txt')
        def eng_():
            webbrowser.open('https://raw.githubusercontent.com/Dhananjay113/AINN/main/energy.txt')
        def dss_():
            webbrowser.open('https://raw.githubusercontent.com/Dhananjay113/AINN/main/data_security.txt')
        
        if(ai>semi and ai>eng and ai>dss ):
            mitemasu = open(r'F:\Dhananjay\Coading\AINN\file\ai.txt', 'r')
            print(mitemasu.read())
            mitemasu.close()
            ai_()
        elif (semi>ai and semi>eng and semi>dss ):
            mitemasu = open(r'F:\Dhananjay\Coading\AINN\file\semi.txt', 'r')    
            print(mitemasu.read())
            mitemasu.close()
            semi_()
        elif (eng>ai and eng>semi and eng>dss ):
            mitemasu = open(r'F:\Dhananjay\Coading\AINN\file\eng.txt', 'r')
            print(mitemasu.read())
            mitemasu.close()
            eng_()
        elif (dss>ai and dss>semi and dss>eng):
            mitemasu = open(r'F:\Dhananjay\Coading\AINN\file\dss.txt', 'r')
            print(mitemasu.read())
            mitemasu.close()
            dss_()
   
    pikachu_button = Button(pikachu,text="Submit",command=palkiya)
    pikachu_button.place(x=100,y=600)

    pokemon.destroy()


nxt_button = Button(pokemon,text="submit",command=rotom)
nxt_button.pack()


    


pokemon.mainloop()
