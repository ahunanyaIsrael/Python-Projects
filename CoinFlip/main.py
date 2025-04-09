import random


playing = True
print("=== 🎮 COIN FLIP GAME 🎮=== \n ✨ Guess heads or tails ✨")

while playing:
    coin = ("heads", "tails") 
    flip = random.choice(coin)
    guess = input("🤔 Enter your guess (heads/tails): ").lower()
    
    if guess not in coin:
        print("❌Invalid options!❌")
        continue


    if flip != guess: print("😢 Sorry, wrong guess. Try Again")
    else: 
        print(f"The coin shows {flip}")
        print("🎉 You guessed correctly!. You win! 🏆")

    choice = input("♻ Play again? (y/n): ").lower()

    if choice == 'y':
        continue
    else:
        print("Thanks for playing! 👋")
        playing = False

