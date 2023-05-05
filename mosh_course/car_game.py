# start - starts the car engine
# stop - stops the car engine
# quit - exits the game
# help - provides list of available commands

command = ""
print(command)

while command.lower() != "quit":
    command = input("> ")
    if command.lower() == "start":
        print("the car engine is running")
    elif command.lower() == "stop":
        print("the car engine is stopped")
    elif command.lower() == "help":
        print("""
        start - this will start the car engine
        stop  - this stops the car engine
        quit  - this ends the car game
        """)
    elif command.lower() == "quit":
        break
    else:
        print("Sorry, I don't understand that command. Try Again.")
