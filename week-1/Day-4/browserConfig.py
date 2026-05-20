#example for encapsulation

class BrowserConfig:
    def __init__(self):
        self.__browser="chrome"
        self.__timeout=30

    def get_config(self):
        print("browser : ",self.__browser)
        print("timeout :", self.__timeout)

    def set_timeout(self,time):
        if time>0:
            print("timeout updated successfully")

        else:
            print("invalid timeout value")

config =BrowserConfig()
config.get_config()
config.set_timeout(60)
config.get_config()
print(config.__timeout)