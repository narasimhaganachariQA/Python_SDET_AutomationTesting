class LoginAutomation:
    def __init__(self):
        self.__username="admin" #private member variables
        self.__password="admin123"

    # print(__username)# can't access private variables
    # print(__password)

    def login(self):
        print("logining into application " )
        print("username : " ,self.__username)
        print("pasasword : ", self.__password)

    def change_password(self, new_password):
        if(len(new_password))>=8:
            self_password=new_password
            print("password updated successfully")
            #print(self_password)
        else:
            print("week password")

test=LoginAutomation()

test.login()
test.change_password("securepass")

#call annd print constructor variables

