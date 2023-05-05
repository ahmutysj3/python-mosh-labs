try:
    age = int(input("Age: "))
    income = 100000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid Value - Integers only please")
except ZeroDivisionError:
    print("Age cannot be zero (0)")