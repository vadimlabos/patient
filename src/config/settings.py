from functools import lru_cache
from pathlib import Path
from pydantic import ConfigDict

from pydantic_settings import BaseSettings


@lru_cache()
def get_general_settings():
    return GeneralSettings()


class GeneralSettings(BaseSettings):
    db_connection_string: str
    db_driver: str

    patient_table: str
    patient_id_table: str
    episode_table: str
    request_table: str

    redis_host: str
    redis_port: int
    redis_db: int

    model_config = ConfigDict(env_file=Path(__file__).parent / "./../.env")
