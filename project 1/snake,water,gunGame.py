import random #Importing random will generate random numbers for computer
'''
 snake -1
 water 0
 gun 1

 '''
computer=random.choice([-1,0,1])
youstr=input("Enter your choice : ") #takes input from user
youdict={"s":-1 ,"w":0 ,"g":1 }      #to assign numbers corresponding to the input given by the user
reversedict={-1:"snake" ,0:"water" ,1:"gun" } #so that we can print the input given by computer and user 

you=youdict[youstr] #storing the numerical value to compare it with computers choice and decide who won
 
print(f"you chose {reversedict[you]} \ncomputer chose {reversedict[computer]}") #printing choice of both computer and the user

if(computer==you):
    print("its a draw")

else:
    if(computer==-1 and you==0):
        print("you lose")
    elif(computer==-1 and you==1):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you win")
    
    else:
        print("something went wrong!!")
