from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
)
from http import HTTPStatus

from fixtures.users import UserFixture
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
import pytest


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient):
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)

    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(response_data, request)

    validate_json_schema(response_data, response.json())


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(
    function_user: UserFixture, private_users_client: PrivateUsersClient
):
    response = private_users_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(response.text)
    create_user_response_data = function_user.response

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_get_user_response(response_data, create_user_response_data)

    validate_json_schema(response_data, response.json())
