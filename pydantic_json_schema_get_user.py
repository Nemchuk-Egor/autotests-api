from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.faker import fake
from tools.assertions.schema import validate_json_schema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string",
)

create_user_response = public_users_client.create_user(create_user_request)
print("Create user data:", create_user_response)


authentication_user = AuthenticationUserSchema(
    email=create_user_request.email, password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)
print("Get user data:", get_user_response.json())
get_user_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(schema=get_user_response_schema, instance=get_user_response.json())
