from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateRequestDict(TypedDict):
    """
    Описание структуры для создания пользователя
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """Клиент для публичных (не требующих авторизации) методов работы с пользователями."""

    def create_user_api(self, request: CreateRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.

        :param request: Словарь с email и password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
