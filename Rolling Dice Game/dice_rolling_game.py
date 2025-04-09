import random

#loop
# Ask: roll the dice
# If user enters y
#   generate two number
#   print them
# If user enter n 
#   print thank you message
#   Terminate
# Else
#   Print invalid Choice

play = int(input("How may times will you want to roll the dice: "))
count = 0
while play > 0:
    choice = input("Roll the dice (y/n): ").lower()
    if choice == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        answer = (dice1, dice2)
        print(answer)
        count += 1
        play -= 1
        if play == 0:
            print("Thank You for Playing")
            print(f"You rolled the dice {count} times")
    elif choice == "n":
         print("Thank You for playing!")
         print(f"You rolled the dice {count} times")
         playing = False
    else : print("Invalid Choice!")


