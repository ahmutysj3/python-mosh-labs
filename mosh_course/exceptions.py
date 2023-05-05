try:
    age = int(input("Age >"))
    print(age)
except ValueError:
    print("You must enter a numerical value")