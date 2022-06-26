from pydantic import BaseSettings
from functools import lru_cache


class Settings:
    class SettingsClass(BaseSettings):
        db: str
        db_name: str
        cookie_name: str
        jwt_algorithm: str
        jwt_secret: str
        user_id: str
        user_name: str
        password: str
        cookie_expires: str

        class Config:
            env_file = ".env"
            env_file_encoding = "utf-8"

    @lru_cache()
    def settings(self):
        return self.SettingsClass()
