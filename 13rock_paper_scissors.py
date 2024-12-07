import random

exit=False
user_point=0
computer_point=0

while exit==False:
 option =["rock","paper","scissors"]
 user_input=input("chose rock ,paper , scissors or exit : ")
 computer_input =random.choice(option)

 if user_input == "exit":
    #  print=True
    print("Game Ended")
    print("you won a toatl of : "+str(user_point)+" and the computer total course : "+str(computer_point))
    exit=True
    # slide cahnge 
 if user_input =="rock": # 1 attemt
   if computer_input=="rock":
       print("your input is rock")     
       print("computer input is rock")     
       print("IT is a tie!") 
 elif computer_input == "paper":
          print("your input is rock")     
          print("computer input is paper")     
          print("Computer wins")
          computer_point +=1
 elif computer_input == "scissors":
          print("your input is rock")     
          print("computer input is scissors")     
          print("ME JIT GAYA wins")
          user_point +=1      

 if user_input =="paper": # 2 attemt
    if computer_input=="rock":
       print("your input is paper")     
       print("computer input is rock")     
       print("ME JIT GAYA wins")
       user_point +=1
    elif computer_input == "paper":
        print("your input is paper")     
        print("computer input is paper")     
        print("it is a tie!")      
    elif computer_input == "scissors":
        print("your input is paper")     
        print("computer input is scissors")     
        print("computer wins")
        computer_point +=1   

 elif user_input =="scissors": # 3 attemt
    if computer_input=="rock":
       print("your input is scissors")     
       print("computer input is rock")     
       print("computer wins")
       computer_point +=1
    
    elif computer_input == "paper":
        print("your input is scissors")     
        print("computer input is paper")     
        print("your win")      
        user_point+=1
    elif computer_input == "scissors":
        print("your input is scissors")     
        print("computer input is scissors")     
        print("it is tie!")


user_input !="rock" or user_input!="paper" or user_input!="scissors" 
print("invalid inputs")
