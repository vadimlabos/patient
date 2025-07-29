from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


@lru_cache()
def get_general_settings():
    return GeneralSettings()


class GeneralSettings(BaseSettings):
    db_connection_string: str
    db_driver: str
    patient_table: str

    class Config:
        env_file = Path(__file__).parent / "./../.env"
