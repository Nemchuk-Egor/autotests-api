from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response
import pytest


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_user_client: PublicUsersClient):
    request = CreateUserRequestSchema()
    response = public_user_client.create_user_api(request)

    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(response_data, request)

    validate_json_schema(response_data, response.json())
