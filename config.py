from decouple import config

class Config:
    DEBUG = config("APP_DEBUG", False, cast=bool)
    APP_NAME = config("APP_NAME", "plangrid_homework", cast=str)
