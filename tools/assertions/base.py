from typing import Any


def assert_status_code(actual: int, expected: int):
    assert actual == expected, (
        "Incorrect status code",
        f"Actual: {actual}, Expected: {expected}",
    )


def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, (
        f"Incorrect value: {name}",
        f"Actual: {actual}, Expected: {expected}",
    )


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, f'Incorrect value: "{name}". Expected true value but got: {actual}'
