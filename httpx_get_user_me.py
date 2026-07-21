import httpx

login_payload = {"email": "user@example.com", "password": "string"}
login_response = httpx.post(
    "http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload
)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Решил использовать клиент, с точки зрения будущего расширения скрипта но наверное на данном этапе будет
# избыточным
client = httpx.Client(
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
)

me_response = client.get("http://127.0.0.1:8000/api/v1/users/me")
me_response_data = me_response.json()

print("Me response", me_response_data)
print("Status Code:", me_response.status_code)

client.close()
