from app.tools.settings import BaseConfig


class ProdConfig(BaseConfig):
    """Production configuration."""

    DB_URI = "postgresql+psycopg2://{}@mig.rosgvard.ru/mig?gssencmode=disable"
    # SWAGGER = {
    #     "swagger": "2.0",
    #     "info": {
    #         "title": "Шаблон",
    #         "description": "Проект шаблон.",
    #         "version": "1.0.0"
    #     },
    #     "schemes": [
    #         "http"
    #     ]
    # }