from pydantic import BaseModel, Field, ConfigDict


class Exercise(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    exercises: list[Exercise]


class GetExerciseResponseSchema(BaseModel):
    exercise: Exercise


class CreateExerciseResponseSchema(BaseModel):
    exercise: Exercise


class UpdateExerciseResponseSchema(BaseModel):
    exercise: Exercise


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """

    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default=None)
    max_score: int | None = Field(alias="maxScore", default=None)
    min_score: int | None = Field(alias="minScore", default=None)
    order_index: int | None = Field(alias="orderIndex", default=None)
    description: str | None = Field(default=None)
    estimated_time: str | None = Field(alias="estimatedTime", default=None)
