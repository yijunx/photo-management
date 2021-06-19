import os
from pydantic import BaseSettings


class Settings(BaseSettings):

    SERVICE_NAME: str
    SERVICE_VERSION: str
    ENV: str

    DATABASE_URI: str

    S3_ACCESS: str
    S3_SECRET: str
    S3_HOST: str
    S3_BUCKET: str


class ProdConfig(Settings):
    pass


class DevConfig(Settings):
    class Config:
        env_file = "./config/dev.env"


def get_conf():
    if os.getenv("ENV"):
        return ProdConfig()
    else:
        return DevConfig()


conf = get_conf()

if __name__ == "__main__":
    print(conf)
