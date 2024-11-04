# Validate Username
# Username can not be more than 12 characters
# Must not contain spaces and digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username can't contain spaces")
elif not username.isalpha():
    print("Username can't contain digits")
else:
    print(f"welcome {username}")