from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import (
    LoginRequestSchema,
    LoginResponseSchema,
)
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from http import HTTPStatus
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
import pytest


@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user: UserFixture, authentication_client: AuthenticationClient):
    request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password,
    )
    response = authentication_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)
    validate_json_schema(response_data, response.json())
