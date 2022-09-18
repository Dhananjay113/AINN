name = str(input(print("Enter yout name :")))
dpt = str(input(print("Enter your department :")))

print("What do you think is the Technology in-demand right now :-")
print("1.Ai\n2.Semiconductors\n3.Energy\n4.Data and Security\n5.Work From Home")
q1 = int(input(print("Ans : ")))

print("What do you think the government ahould invest on if it had a billion doller :-")
print("1.Improve our military\n2.Do something to improve the income\n3.Invest in manufacturing\n4.have it as a back up\n5.Give it for free to the people")
q2 = int(input(print("Ans : ")))

print("Who do you like in thi list :- ")
print("1.Iscac Newton\n2.Gausess\n3.Ted Hoff\n4.Satoshi Nakamoto\n5.Joe Biden")
q3 = int(input(print("Ans : ")))

print("Which of these companies do you like in this list :- ")
print("1.Google\n2.Tesla\n3.Intel\n4.IBM\n5.Toie")
q4 = int(input(print("Ans : ")))

print("what would you do from the given options in your freetime :- ")
print("1.Cycle\n2.Code\n3.Play with PCBs\n4.Scout\n5.Sleep")
q5 = int(input(print("Ans : ")))

ai = 0 
semi = 0 
eng = 0 
dss = 0
uf = 0



match q1:
    case 1: ai+=1; 
    case 2: semi+=1
    case 3: eng+=1
    case 4: dss+=1
    case 5: uf+=1
    
match q2:
    case 1: dss+=1
    case 2: eng+=1
    case 3: semi+=1
    case 4: ai+=1
    case 5: uf+=1

match q3:
    case 1: ai+=1
    case 2: eng+=1
    case 3: semi+=1
    case 4: dss+=1
    case 5: uf+=1

match q4:
    case 1: ai+=1
    case 2: eng+=1
    case 3: semi+=1
    case 4: dss+=1
    case 5: uf+=1

match q5:
    case 1: eng+=1
    case 2: ai+=1
    case 3: semi+=1
    case 4: dss+=1
    case 5: uf+=1
    
print(ai,dss,eng,semi,uf)
        
if(ai>semi and ai>eng and ai>dss and ai>uf):
    mitemasu = open(r'F:\Dhananjay\Coading\AINN\ai.txt', 'r')
    print(mitemasu.read())
    mitemasu.close()  
    
elif (semi>ai and semi>eng and semi>dss and  semi>uf):
    mitemasu = open(r'F:\Dhananjay\Coading\AINN\Embedded_systems.txt', 'r')
    print(mitemasu.read())
    mitemasu.close()

elif (eng>ai and eng>semi and eng>dss and eng>uf):
    mitemasu = open(r'F:\Dhananjay\Coading\AINN\energy.txt', 'r')
    print(mitemasu.read())
    mitemasu.close()

elif (dss>ai and dss>semi and dss>eng and dss>uf):
    mitemasu = open(r'F:\Dhananjay\Coading\AINN\data_security.txt', 'r')
    print(mitemasu.read())
    mitemasu.close()

elif (uf>dss and uf>ai and uf>eng and uf>semi):
    print("YOU ARE UNFIT TO BE AN ENGINNERE")   