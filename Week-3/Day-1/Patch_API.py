import requests

# API URL
url = "https://dummyjson.com/users/26"

# Updated Payload
payload = {
     
        "age": 99,
      
}

# Send PUT Request
response = requests.patch(url, json=payload)

# Convert response to JSON
data = response.json()

# Print response details
print("Status Code:", response.status_code)

print("\nUpdated Product Details")
print("-------------------------")

print("age:", data["age"])

# Validations
assert response.status_code == 200

assert data["age"] == 99

print("\nPUT API Test Passed")