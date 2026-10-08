from typing import Any, Sized
import allure
from tools.logger import get_logger


logger = get_logger("BASE ASSERTION")


@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int):

    logger.info(f"Check that response status code equals to {expected}")

    assert actual == expected, (
        "Incorrect status code",
        f"Actual: {actual}, Expected: {expected}",
    )


@allure.step("Check that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):

    logger.info(f"Check that {name} equals to {expected}")

    assert actual == expected, (
        f"Incorrect value: {name}",
        f"Actual: {actual}, Expected: {expected}",
    )


@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    logger.info(f"Check that {name} is true")

    assert actual, f'Incorrect value: "{name}". Expected true value but got: {actual}'


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    with allure.step(f"Check that length of {name} equals to {len(expected)}"):
        logger.info(f"Check that length of {name} equals to {len(expected)}")
        assert len(actual) == len(expected), (
            f'Incorrect object length: "{name}". '
            f"Expected length: {len(expected)}. "
            f"Actual length: {len(actual)}"
        )
