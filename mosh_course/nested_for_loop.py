for x in range(10):
    for y in range(5):
        print(f"({x},{y})")
 
 
# Method 1       
""" numbers = [5,2,5,2,2]

for i in numbers:
    print(i * "x") """
    
# Method 2 with Inner loop

list = [5,2,5,2,2]

for number in list:
    output = ""
    for count in range(number):
        output += ":)"
    print(output)