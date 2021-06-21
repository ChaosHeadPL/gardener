from pydantic import BaseSettings


class Settings(BaseSettings):
    log_level = "Debug"
    log_file = "service.log"
    BASE_URL = "127.0.0.1:8000"