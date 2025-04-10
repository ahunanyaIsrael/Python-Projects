import random
import time
import os


def clear_screan():
    """
        Clears the terminal screen
    """
    os.system("cls" if os.name == "nt" else "clear")

print("\n=== 🧠 MEMORY SEQUENCE GAME 🧠 ===")
print("✨Remember the sequence and type it back! ✨")
print("\nRules")
print("-Watch as many numbers apear on by one")
print("-After the sequence is shown, type it back in order")
print("-Each round add one more number to remember")
print("-How far can you go\n")

input("pres enter to start....")

sequence = []
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1, 9))

    clear_screan() 

    print(f"\n=== Round {current_round}")
    print(f"Remember this sequence of {len(sequence)} numbers: ")
    # print out the sequence in the list 
    for num in sequence:
        time.sleep(2)
        print(f"\n{num}")
        time.sleep(2)
        clear_screan()

    print("\nNow repeat the sequence by typeing each number, seperated by spaces")
    player_answer = input("> ")

    # "3,6,1" => ["3", "6", "1"]
    #Convert to an a list  using the split the change data type it int
    try:
        player_sequnence = [int(num) for num in player_answer.split()] 

    except ValueError:
        print("Please enter number only")
        game_over = True
        continue
    # conpare numbers for equallity 
    if player_sequnence == sequence:
        print(f"🎉 Congrats you remembered all {len(sequence)} numbers")
        current_round += 1
        time.sleep(2)
    else:
        print(f"Game over! You rmemembered {current_round - 1} numbers")
        print(f"The correct sequence was {"".join(str(num) for num in sequence)}")
        game_over = True

    if game_over:
        play_again = input("Play again? (y/n)").lower()
        if play_again == "y":
            sequence = []
            current_round = 1
            game_over = False

        else:
            print("Thanks for playing")