import random
randnum = int(random.random()*100)
user= int(input("Enter the number: "))
count=1
while(user!=randnum):
    count+=1
    if(user<randnum):
        print("Too Low")
    elif(user>randnum):
        print("Too High")
    user= int(input("Wrong guess , Guess another number: "))
if(randnum==user):
    print("Correct Answer is",randnum,"you guessed it in",count ,"attempts")
    
    