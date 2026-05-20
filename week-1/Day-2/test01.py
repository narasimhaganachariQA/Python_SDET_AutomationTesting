# #username=input("Enter user : ").strip().lower()

# username="narasimha"
# char1=username[0].upper()
# username =char1+username[1:len(username)]
# print(username)


# print(username)
# print("username : ", username)
# print("Length : ", len(username))
# print("starts with : ", username[0].isalnum())
# print("Alphanumeric : ", username.isalnum())
# print("Name format : ", username[0].upper() )


#Example: 2

while True:
    try:
        username=input("Enter username : ").strip().lower()
        password =input("Enter password : ").strip()

        #validation user assert
        assert username == "admin"
        assert password == "Admin@123"
        print("login successful")
        break

    except AssertionError:
        print("Invalid username or password")