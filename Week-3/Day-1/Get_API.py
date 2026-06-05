# Import required libraries
import requests
import json
# url="https://dummyjson.com/products"

# #send the https Get request
# response=requests.get(url)

# #print the raw status code and Json data for visbilty
# print(f"Status code : {response.status_code}")

# print("Json response Body:")
# json_data=response.json()

# first_product=json_data["products"][2]

# print("\n first Product Details")
# print("-------------------------")
# print("Tile: ", first_product["title"])
# print("Price :",first_product["price"])
# print("Category :",first_product["category"])
#print("")

url="https://dummyjson.com/users"

#send the https Get request
response=requests.get(url)

#print the raw status code and Json data for visbilty
print(f"Status code : {response.status_code}")

print("Json response Body:")
json_data=response.json()

first_product=json_data["users"][25]  #Chaining user to 25 id 

print("\n first user Details")
print("-------------------------")
print("firstName: ", first_product["firstName"])
print("lastName :",first_product["lastName"])
print("lastName :",first_product["lastName"])
print("age :",first_product["age"])

# Validation
if response.status_code == 200:
    print("\nAPI Test Passed")
else:
    print("\nAPI Test Failed")