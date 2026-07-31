from typing import Any, Sized


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


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    assert len(actual) == len(expected), (
        f'Incorrect object length: "{name}". '
        f"Expected length: {len(expected)}. "
        f"Actual length: {len(actual)}"
    )
