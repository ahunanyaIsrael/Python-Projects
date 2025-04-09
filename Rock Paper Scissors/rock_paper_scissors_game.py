import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {
        ROCK : "🤘",
        PAPER : "📃",
        SCISSORS : "✂"
    }
choice = tuple(emojis.keys())
def winner(user_choice, computer_choice):
    if user_choice == computer_choice: print("Tie!")
    elif (user_choice == ROCK and computer_choice == SCISSORS) or (user_choice == SCISSORS and computer_choice == PAPER) or (user_choice == PAPER and computer_choice == ROCK): 
        print("You win")
    print("You Lose!")



def get_user_choice():
    while True:
        user_choice  = input("Rock, Paper, Scssors? (r/p/s)").lower()
        if user_choice not in choice: 
            return user_choice
        return user_choice

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")


def play():

    # Ask te user to make a choice
    # if choice is invalid 
    #   print an error
    #Let computer to make a choice
    # Print choices using imojis
    # Determine the winner
    # Ask if user want to continue
    #If not 
    #   Terminate the game
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choice)
        display_choices(user_choice, computer_choice)
        winner(user_choice, computer_choice)
        should_continue = input("Do you want to continue? (y/n)").lower()
        if should_continue == 'n' : break
        
play()
