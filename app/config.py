import os
from typing import Union
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str


class Dev(Settings):
    ENVIRONMENT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str


class Prod(Settings):
    ENVIRONMENT: str


config = dict(development=Dev, production=Prod)


settings: Union[Dev, Prod] = config[os.environ.get("ENVIRONMENT").lower()]()
