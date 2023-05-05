# Username Length

print("Please update your username")
print("Usernames are not case-sensitive")
username = input("Enter username here: ")

# this block will return different error messages based on the length of the username input
if len(username) > 50:
    print(f"That username is " + str(len(username) - 50) + " " + "characters too long. Choose something shorter than 50 characters.")
elif len(username) < 3:
    print("That username is " + str(3 - len(username)) + " " + "characters too short. Choose something longer than 3 characters.")
else:
    print("That password is a good length.")