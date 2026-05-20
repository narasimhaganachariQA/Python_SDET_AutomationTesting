with open("credentials.txt", "r") as file:
    for line in file:
        username,password=line.strip().split(",")
        print("Executing login Test")

        print("user name :", username)
        print("password : ", password)