from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
)
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercise import (
    assert_create_exercise_response,
    assert_get_exercise_response,
    assert_update_exercise_response,
    assert_exercise_not_found_response,
    assert_get_exercises_response,
)
from tools.assertions.schema import validate_json_schema
from tools.assertions.errors import InternalErrorResponseSchema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(
        self, exercises_client: ExercisesClient, function_course: CourseFixture
    ):
        """
        Проверяет успешное создание задания через API.
        - Отправляется POST-запрос с course_id.
        - Проверяется статус-код 200.
        - Проверяется соответствие тела ответа запросу.
        - Валидируется JSON-схема ответа.
        """

        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture,
    ):
        """
        Проверяет успешное получение задания по ID.
        - Создаётся задание через фикстуру.
        - Выполняется GET-запрос с его ID.
        - Проверяется статус-код 200.
        - Сравнивается полученное задание с созданным.
        - Валидируется JSON-схема ответа.
        """

        exercise_id = function_exercise.response.exercise.id
        response_exercise = function_exercise.response
        response = exercises_client.get_exercise_api(exercise_id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, response_exercise)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ):
        """
        Проверяет успешное обновление задания через API.
        - Создаётся задание через фикстуру.
        - Выполняется PATCH-запрос с его ID и новыми данными.
        - Проверяется статус-код 200.
        - Проверяется соответствие тела ответа запросу.
        - Валидируется JSON-схема ответа.
        """
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(
            function_exercise.response.exercise.id, request
        )
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(response_data, request)
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_exercise(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ):
        """
        Проверяет успешное удаление задания.
        - Удаляется задание через DELETE-запрос.
        - Проверяется статус-код 200.
        - Затем выполняется GET-запрос по тому же ID.
        - Проверяется статус-код 404 и сообщение об ошибке.
        - Валидируется JSON-схема ошибки.
        """
        exercise_id = function_exercise.response.exercise.id

        delete_response = exercises_client.delete_exercise_api(exercise_id)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(exercise_id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(
            get_response.text
        )

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    def test_get_exercises(
        self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture,
        function_course: CourseFixture,
    ):
        course_id = GetExercisesQuerySchema(
            courseId=function_exercise.response.exercise.course_id
        )

        response = exercises_client.get_exercises_api(course_id)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])

        validate_json_schema(response.json(), response_data.model_json_schema())
