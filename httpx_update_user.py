import httpx
from tools.faker import fake

users_create_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}
users_create_response = httpx.post(
    "http://127.0.0.1:8000/api/v1/users", json=users_create_payload
)
users_create_response_data = users_create_response.json()
print("Status Code:", users_create_response.status_code)
print("Users response", users_create_response_data)

login_payload = {
    "email": users_create_payload["email"],
    "password": users_create_payload["password"],
}
login_response = httpx.post(
    "http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload
)
login_response_data = login_response.json()
print("Status Code:", login_response.status_code)
print("Login response", login_response_data)

get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
users_id_payload = users_create_response_data["user"]["id"]
users_updated_payload = {
    "email": fake.email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}
users_updated_response = httpx.patch(
    f"http://127.0.0.1:8000/api/v1/users/{users_id_payload}",
    headers=get_user_headers,
    json=users_updated_payload,
)
users_updated_response_data = users_updated_response.json()
print("Status Code:", users_updated_response.status_code)
print("Users updated", users_updated_response_data)
