import random
# Generate a radom number
# Ask user to make a guess
# if not a valid number
#   print an error
# if number < guess
#print Too low
#If number > guess
#   print Too high
# else Well done


rand_ans = random.randint(1, 100)
print(rand_ans)
playing = True
while playing:
    try:
        number = int(input("Guess a number between 1 and 100: "))

        # assert number >= 0 , "guess is lower than 0"
        # assert number <= 100, "guess is higher than 100"

        if not 1 <= number <= 100:
            print("Please enter a number between 1 and 100.")
            continue

            
        if number > rand_ans: print("Too high!")
        elif number <rand_ans: print("Too low!")
        else: 
            print("Congratulations! you guessed the number")
            playing = False
    except ValueError :
        print("Please enter a valid number")

    