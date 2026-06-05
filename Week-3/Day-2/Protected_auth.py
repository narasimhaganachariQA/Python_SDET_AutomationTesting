#After login, use token in protected API.

import requests

# Protected API
url = "https://dummyjson.com/auth/me"

# Token received from login API
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJlbWlseXMiLCJlbWFpbCI6ImVtaWx5LmpvaG5zb25AeC5kdW1teWpzb24uY29tIiwiZmlyc3ROYW1lIjoiRW1pbHkiLCJsYXN0TmFtZSI6IkpvaG5zb24iLCJnZW5kZXIiOiJmZW1hbGUiLCJpbWFnZSI6Imh0dHBzOi8vZHVtbXlqc29uLmNvbS9pY29uL2VtaWx5cy8xMjgiLCJpYXQiOjE3Nzk4NzY3MjUsImV4cCI6MTc3OTg4MDMyNX0.QNvSwhdVf2KntSWSovOHH2y37omnQKwSF5-poICUNV4"

# Authorization Header
headers = {
    "Authorization": f"Bearer {token}"
}

# Send GET request
response = requests.get(url, headers=headers)

# Print response
print(response.status_code)
print(response.json())