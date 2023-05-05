""" sodas = ["pepsi","coke","sprite","fanta"]
print(sodas[0])

sodas[0] = "Pepsi"
print(sodas) """

numbers = [1,5,2,3,3,9,10]
max = numbers[0]
print(max)

for item in numbers:
    if item > max:
        max = item
        
print(max)