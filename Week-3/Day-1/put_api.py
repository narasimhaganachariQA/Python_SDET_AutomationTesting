import requests

# API URL
url = "https://dummyjson.com/users/26"

# Updated Payload
payload = {
     
      "firstName": "Evelyn",
      "lastName": "Gonzalez",
      "maidenName": "test",
      "age": 99,
      "gender": "male"
}

# Send PUT Request
response = requests.put(url, json=payload)

# Convert response to JSON
data = response.json()

# Print response details
print("Status Code:", response.status_code)

print("\nUpdated Product Details")
print("-------------------------")
print("firstName:", data["firstName"])
print("maidenName:", data["maidenName"])
print("gender:", data["gender"])
print("age:", data["age"])

# Validations
assert response.status_code == 200
assert data["gender"] == "male"
assert data["age"] == 99

print("\nPUT API Test Passed")