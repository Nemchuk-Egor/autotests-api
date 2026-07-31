from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema
from tools.assertions.base import assert_equal

def assert_create_exercise_response(actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema):
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
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")
    