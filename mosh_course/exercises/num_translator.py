phone_map = {
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"  
}
phone_number = input("Phone Number: ")

output = ""
for number in phone_number:
    output += phone_map.get(number,"!") + " "
    
print(output)