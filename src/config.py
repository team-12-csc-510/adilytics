from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Adilytics"

    class Config:
        env_file = ".env"
