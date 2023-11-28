from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_db: str = "db_name"
    postgres_user: str = "username"
    postgres_password: str = "password"
    postgres_port: int = 5432
    sqlalchemy_database_url: str ="postgresql+psycopg2://username:password@localhost:5432/db_name"
    secret_key: str = "secret key"
    algorithm: str = "algotihtm"
    mail_username: str = "example@meta.ua"
    mail_password: str = "password"
    mail_from: str = "example@meta.ua"
    mail_port: int = 465
    mail_server: str = "smtp.meta.ua"
    redis_host: str = "localhost"
    redis_port: int = 6379
    cloudinary_name: str = "cloudinary name"
    cloudinary_api_key: str = "key"
    cloudinary_api_secret: str = "secret"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
