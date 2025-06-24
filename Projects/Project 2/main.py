import random

count=0
def computer_chose():
    c=random.randint(1,30)
    return int(c)
def users_choice():
    n=input("Choose a number: ")
    if n.upper()=="Q":
        return "Q"
    else:

        return int(n)

def guessing(user,computer):
    global count
    count+=1
    if(computer==user):
        print("Prefect you guessed it right!")
        return True
    elif(computer>user):
        print("Try higher!")
    elif(computer<user):
        print("Try lower!")
    return False    

def play_game(computer):
    print("Welcome to the Guessing game!")
    
    while True:
        user= users_choice()
        if user =="Q":
            print("You quit the game")
            break
        elif user is None or not 1<=user<=30:
            print("Pick a number between 1-30")
            continue
        if(guessing(user,computer)):
            break
    print(f"NO. of guesses you took: {count}")
    return computer
        
    
comp=computer_chose()

play_game(comp)