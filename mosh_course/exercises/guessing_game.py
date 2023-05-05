# 3 chances to guess number between 1 and 10

secret_num = 5
print("welcome to the guessing game. Pick a number between 1 and 10.")
print("you have 3 guesses!")
guess_count = 0
guess_limit = 3

# Method 1 using incrementing count w/o break
""" while guess_count < guess_limit:
    guess = int(input("Guess: "))
    
    if guess == secret_num:
        print("Thats correct! Good Guess.")
        guess_count += guess_limit # this increments guess_count over the limit to end the game
        
    else:
        print("Wrong!")
        guess_count += 1
        print("You have " + str(guess_limit - guess_count) + " guesses left") # prints the number of guesses left
        
if guess_count >= guess_limit:
    print("Thanks for playing!") """
    
# Method 2 using break

while guess_count < guess_limit:
    guess = int(input("Guess " + str(guess_count + 1) + ": "))
    guess_count += 1
    
    if guess == secret_num:
        print("That's correct! You guessed the number.")
        break
    else:
        print("Wrong!")
        print("You have " + str(guess_limit - guess_count) + " guesses left")
else:
    print("Sorry, you ran out of guesses.")
    
print("Thanks for playing!")