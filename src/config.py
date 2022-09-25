from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Adilytics"

    class Config:
        env_file = ".env"
