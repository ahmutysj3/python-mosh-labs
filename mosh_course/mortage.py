# Mortage Down Payment Calculator

print("Welcome to the down payment calculator")
has_good_credit = input("Do you have good credit? (answer 'yes' or 'no'): ")

if has_good_credit == "yes":
    has_good_credit = True
elif has_good_credit == "no":
    has_good_credit = False

house_price = 1000000

if has_good_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2

print("Your down payment will be " + "$" + str(down_payment))
print(f"The down payment for the house is ${down_payment}, have a nice day")
