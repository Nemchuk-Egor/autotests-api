from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
)
from tools.assertions.base import assert_status_code
from http import HTTPStatus
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema


def test_login():
    public_user_client = get_public_users_client()

    create_user_request_schema = CreateUserRequestSchema()
    create_user_response = public_user_client.create_user(create_user_request_schema)

    authentication_client = get_authentication_client()
    login_request = LoginRequestSchema(
        email=create_user_request_schema.email,
        password=create_user_request_schema.password,
    )
    login_response = authentication_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
    validate_json_schema(login_response_data, login_response.json())
