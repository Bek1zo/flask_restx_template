"""Debug setting."""

from app.tools.settings import BaseConfig


class DevConfig(BaseConfig):
    """Development configuration."""

    # DB_URI = "postgresql+psycopg2://prikazovpp:password@192.168.128.250:5442/mig"
    DB_URI = 'sqlite:///data_base.db?check_same_thread=False'