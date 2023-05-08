# rule 1: if the number is divisible by 3 then it returns Fizz
# rule 2: if the number is divisible by 5 then it returns Buzz
# rule 3: if the number is divisible by both 3 and 5 then it returns FizzBuzz
# rule 4: any other number just returns the number

# def fizz_buzz(input):
#     if input % 3 == 0 and input % 5 != 0:
#         print("Fizz")
#     elif input % 5 == 0 and input % 3 != 0:
#         print("Buzz")
#     elif input % 3 == 0 and input % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(input)

# print(fizz_buzz(45))

letters = ["e", "a", "a", "r", "b", "m", "c", "d"]

result = letters.count("a")
result = letters.index("r")
# result = letters.pop(1)
# result = letters.append("Z")
result = letters.copy()
# result = letters.remove("a")
# result = letters.reverse()
result = letters.insert(2, "A")
print(result)
print(letters)
