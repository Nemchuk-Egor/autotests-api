from clients.exercises.exercises_schema import (
    CreateExerciseResponseSchema,
    CreateExerciseRequestSchema,
    Exercise,
    GetExerciseResponseSchema,
    UpdateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
)
from tools.assertions.base import assert_equal
from tools.assertions.errors import (
    InternalErrorResponseSchema,
    assert_internal_error_response,
)


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


def assert_exercise(actual: Exercise, expected: Exercise):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(
    actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema
):
    assert_exercise(actual.exercise, expected.exercise)


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


def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(detail="Exercise not found")

    assert_internal_error_response(actual, expected)
