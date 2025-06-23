import random
win_map={
        "Rock":"Scissor",
        "Paper":"Rock",
        "Scissor":"Paper"
    }
Computer_wins=0
user_wins=0
draws=0
choices=list(win_map.keys())




def computers_choice():
    return random.choice(choices)

def users_choice():
    i=input("\nChoose Rock/Paper/Sissor(press q to quit): ").capitalize()
    return i


def who_won_the_round(user,computer):
    global user_wins,Computer_wins,draws
    if(user==computer):
        draws+=1
        return ("It's a Draw\n")
    else:
        if(win_map[user]==computer):
            user_wins+=1
            return ("You won!\n")
        else:
            Computer_wins+=1
            return ("You Lose!\n")

def final_scores():
    if(Computer_wins==user_wins):
        result="Whole game was a Draw"
    elif(Computer_wins>user_wins):
        result="Computer won the Game, Better Luck next time!"
    else:
        result="Congrats You won the Game!"
    return f"\n{result}\nNo.of times computer won: {Computer_wins}\nNo.of time user won: {user_wins}\nNo. of draws: {draws}"

def round_scores():
    return f"\nNo.of times computer won: {Computer_wins}\nNo.of time user won: {user_wins}\nNo. of draws: {draws}"


def play_game():
    print("Welcome to Rock, Paper, Scissor!")
    print("Enter 'q' at any time to quit.\n")
    while True:
        user=users_choice()
        if user=="Q":
            break
        elif user not in choices:
            print("Enter a valid choice!")
            continue
        computer=computers_choice()

        print(f"user chose {user} and the computer chose {computer}")

        print(who_won_the_round(user,computer))
        print(round_scores())
    print("Game over")
    print(final_scores())

play_game()






    

        
