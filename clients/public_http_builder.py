from httpx import Client
from clients.curl_event_hook import curl_event_hook

def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        event_hooks={"request": [curl_event_hook]},
        )
