from pydantic import BaseModel, Field, ConfigDict
from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema


class Course(BaseModel):
    """
    Описание структуры курса.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore", default=0)
    min_score: int = Field(alias="minScore", default=0)
    description: str
    preview_file: FileSchema = Field(alias="previewFile")  # Вложенная структура файла
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(
        alias="createdByUser"
    )  # Вложенная структура пользователя


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """

    user_id: str = Field(alias="userId")


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore", default=0)
    min_score: int = Field(alias="minScore", default=0)
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """

    course: Course


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default=None)
    max_score: int | None = Field(alias="maxScore", default=None)
    min_score: int | None = Field(alias="minScore", default=None)
    description: str | None = Field(default=None)
    estimated_time: str | None = Field(alias="estimatedTime", default=None)
