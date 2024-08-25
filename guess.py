import random
list=["Rock","Paper","Scissors"]
play = "y"
computer_score=0
user_score=0
while(play!="n"):
    rand = int(random.random()*3)
    computer = list[rand]
    user = int(input("Enter the number 0-Rock 1-paper 2-Scissors: "))
    if(user==10):
        play='n'
        break
    try:
        user_guess = list[user]
    except Exception:
        print("out of range")
    if(computer==user_guess):
        print("Its a tie","Com :" ,computer_score,"user: ",user_score)
    else:
        if(computer=="Rock" and user_guess=='Scissors'):
            computer_score+=2
            print("Rock,Computer won","Com :" ,computer_score,"user: ",user_score)
        elif(computer=="Scissors" and user_guess=='Rock'):
            user_score+=2
            print("Computer guess is Scissors so You won","Com :" ,computer_score,"user: ",user_score)
        elif(computer=="Scissors" and user_guess=='Paper'):
            computer_score+=2
            print("Scissors , Computer Won","Com :" ,computer_score,"user: ",user_score)
        elif(computer=="Paper" and user_guess=='Scissors'):
            user_score+=2
            print("Computer guess is Paper so You won","Com :" ,computer_score,"user: ",user_score)
        elif(computer=="Paper" and user_guess=="Rock"):
            computer_score+=2
            print("Computer guess is Rock you won","Com :" ,computer_score,"user: ",user_score)
        else:
            user_score+=2
            print("Computer guess is paper Computer won","Com :" ,computer_score,"user: ",user_score)
        
if(computer_score>user_score):
    print("you lost with ",computer_score-user_score, "points")
elif(computer_score==user_score):
    print("Its a tie")
else:
    print("you won with",user_score-computer_score,"points")

