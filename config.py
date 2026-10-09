from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Self
import platform
import sys


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_png_file: FilePath


class PythonVersionConfig(BaseModel):
    python_version: str


class PlatformSystemConfig(BaseModel):
    info: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )
    test_data: TestDataConfig
    http_client: HTTPClientConfig
    allure_results_dir: DirectoryPath
    python_version: PythonVersionConfig
    os_info: PlatformSystemConfig

    @classmethod
    def initialization(cls) -> Self:
        allure_results_dir = DirectoryPath("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)
        return Settings(
            allure_results_dir=allure_results_dir,
            python_version=PythonVersionConfig(python_version=sys.version),
            os_info=PlatformSystemConfig(
                info=f"{platform.system()}, {platform.release()}"
            ),
        )


settings = Settings.initialization()

