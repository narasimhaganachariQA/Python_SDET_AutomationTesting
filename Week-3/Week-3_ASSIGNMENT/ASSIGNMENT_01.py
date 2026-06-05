# Import requests library
import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users/1"

# Send GET request
response = requests.get(url)

# Validate Status Code
if response.status_code == 200:
    print("PASS: Status Code is 200")
else:
    print("FAIL: Status Code is not 200")

# Convert response into JSON
data = response.json()


# Print JSON Response
print(data)

# Validate specific fields
if data["id"] == 1:
    print("PASS: User ID validated")
else:
    print("FAIL: User ID validation failed")

if data["name"] == "Leanne Graham":
    print("PASS: Name validated")
else:
    print("FAIL: Name validation failed")