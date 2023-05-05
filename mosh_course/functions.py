def greet_user():
    print("hey trace")
    print("nice to meet you")


print("start test")
greet_user()
print("end of test")

#

def greet_user_improved(first_name,last_name):
    print(f"Hi {first_name} {last_name}!")
    print("how are you?")



greet_user_improved("Bill","Smith")
greet_user_improved(last_name="smith",first_name="bob")
print("End of Program")