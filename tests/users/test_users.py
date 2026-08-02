from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
)
from http import HTTPStatus
from tools.faker import fake

from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory
from fixtures.users import UserFixture
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
import pytest
import allure


@pytest.mark.users
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.FILES)
class TestUsers:
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.title("Create User")
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        allure.dynamic.title(f"Attempt to create user with email: {email}")
        email = fake.email(domain=email)
        request = CreateUserRequestSchema(email=email)
        response = public_users_client.create_user_api(request)

        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(response_data, request)

        validate_json_schema(response_data, response.json())

    @allure.story(AllureStory.GET_ENTITY)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.title("Get User me")
    def test_get_user_me(
        self, function_user: UserFixture, private_users_client: PrivateUsersClient
    ):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)
        create_user_response_data = function_user.response

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, create_user_response_data)

        validate_json_schema(response_data, response.json())
