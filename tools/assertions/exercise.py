from clients.exercises.exercises_schema import (
    CreateExerciseResponseSchema,
    CreateExerciseRequestSchema,
    Exercise,
    GetExerciseResponseSchema,
    UpdateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    GetExercisesResponseSchema,
)
from tools.assertions.base import assert_equal
from tools.assertions.errors import (
    InternalErrorResponseSchema,
    assert_internal_error_response,
)
from tools.assertions.base import assert_length
import allure


@allure.step("Check create exercise response")
def assert_create_exercise_response(
    actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema
):
    """
    Проверяет, что ответ на создание задания соответствует запросу.
    Сравниваются все поля: заголовок, идентификатор курса, баллы, описание, порядковый индекс, оценочное время.
    """

    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(
        actual.exercise.estimated_time, expected.estimated_time, "estimated_time"
    )


@allure.step("Check exercise")
def assert_exercise(actual: Exercise, expected: Exercise):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Check get exercise response")
def assert_get_exercise_response(
    actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema
):
    assert_exercise(actual.exercise, expected.exercise)


@allure.step("Check update exercise response")
def assert_update_exercise_response(
    actual: UpdateExerciseResponseSchema, expected: UpdateExerciseRequestSchema
):
    """
    Проверяет, что ответ на обновление задания соответствует запросу.
    Сравниваются все поля: заголовок, баллы, описание, порядковый индекс, оценочное время.
    """
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(
        actual.exercise.estimated_time, expected.estimated_time, "estimated_time"
    )


@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(detail="Exercise not found")

    assert_internal_error_response(actual, expected)


@allure.step("Check get exercises response")
def assert_get_exercises_response(
    get_exercises_response: GetExercisesResponseSchema,
    create_exercise_response: list[CreateExerciseResponseSchema],
):

    assert_length(
        get_exercises_response.exercises, create_exercise_response, "exercises"
    )

    for index, create_exercise_response in enumerate(create_exercise_response):
        assert_exercise(
            get_exercises_response.exercises[index], create_exercise_response.exercise
        )
