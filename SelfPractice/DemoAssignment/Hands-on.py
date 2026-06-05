users=[
    ["admin","admin123"],
    ["test","test123"],
    ["qa","qa123"],
    ["auto","auto123"]
]

for user in users:
    username=user[0]
    password=user[1]

    print("\n checking user : "+username)

    if len(username)>=5: 
       
       if len(password)>=6:
           
           print("valid password")
        
        else:
           print("Invalid password")
    
    else:
         print("invalid user")  

              