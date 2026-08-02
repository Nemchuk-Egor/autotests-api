from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
    UserSchema,
)
from tools.assertions.base import assert_equal
import allure


@allure.step("Check create user response")
def assert_create_user_response(
    response: CreateUserResponseSchema, request: CreateUserRequestSchema
):
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")


@allure.step("Check get user response")
def assert_get_user_response(
    get_user_response: GetUserResponseSchema,
    create_user_response: CreateUserResponseSchema,
):
    assert_user(get_user_response.user, create_user_response.user)
