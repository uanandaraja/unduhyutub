from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Unduhyutub"
    PROJECT_VERSION: str = "1.0.0"
    DOWNLOAD_DIR: str = "./downloads"

settings = Settings()
