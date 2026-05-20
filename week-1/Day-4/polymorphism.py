class crome():
    def launch(self):
        print("crome browser launched")

class Edge():
    _edg="edge"
    def launch(self):
        print("Edge launched")

class firefox():
   __d="firefox"
   def launch(self):
        print("firefox launched")
    

# browsers =[crome(),Edge(),firefox()]

# for browser in browsers:
#     browser.launch()
edg=Edge()
print(edg._edg)
ff=firefox()
print(ff.__d)
    