import textwrap

help_menu = """
    start - starts the car engine
    stop - stops the car engine
    quit - exits the game
    help - provides list of available commands
"""
help_menu_no_indents = textwrap.dedent(help_menu) # this removes the indents from above multi-line string

command = ""
print(command)

# Method #1 using binary for engine status
""" engine_key = 0

while True:
    command = input("> ").lower()
    if command == "start" and engine_key == 0:
        engine_key += 1
        print("the car engine is running")
    elif command == "start" and engine_key > 0:
        print("The car is already on!")
    elif command == "stop" and engine_key > 0:
        engine_key -= 1
        print("the car engine is stopped")
    elif command == "stop" and engine_key == 0:
        print("The car was already turned off!")
    elif command == "help":
        print(help_menu_no_indents)
    elif command == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Sorry, I don't understand that command. Try Again.") """

# Method #2 using bool for engine status plus repeated conditionals

""" engine_started = False

while True:
    command = input("> ").lower()
    if command == "start" and engine_started == False:
        engine_started = True
        print("the car engine is running")
    elif command == "start" and engine_started == True:
        print("The car is already on!")
    elif command == "stop" and engine_started == True:
        engine_started = False
        print("the car engine is stopped")
    elif command == "stop" and engine_started == False:
        print("The car was already turned off!")
    elif command == "help":
        print(help_menu_no_indents)
    elif command == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Sorry, I don't understand that command. Try Again.") """
        

# Method #3 using bool for engine status but without extra repetition

engine_started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if engine_started:
            print("The car is already on!")
        else:
            engine_started = True
            print("The car engine is now running.")
    elif command == "stop":
        if not engine_started:
            print("The car was already turned off!")
        else:
            engine_started = False
            print("the car engine is stopped")
    elif command == "help":
        print(help_menu_no_indents)
    elif command == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Sorry, I don't understand that command. Try Again.")