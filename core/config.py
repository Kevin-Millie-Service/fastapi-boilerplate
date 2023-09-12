from pydantic.v1 import BaseSettings


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "millie-openapi"

    DATABASE_HOST: str = ''
    DATABASE_USER: str = ''
    DATABASE_PASSWORD: str = ''
    DATABASE_NAME: str = ''
    DATABASE_URI = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'


settings = Settings()
