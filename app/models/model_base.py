"""Core models."""
from sqlalchemy import Column, TEXT, TIMESTAMP
from sqlalchemy.sql.expression import func
from . import Base


class BaseClass(Base):
    """Базовый класс для формирования основных таблиц"""

    __abstract__ = True

    # id = Column(TEXT, primary_key=True, nullable=False, server_default=func.public.uuid_generate_v4())
    # created_utc = Column(TIMESTAMP(timezone=False), server_default=func.now(), nullable=False)
    # updated_utc = Column(TIMESTAMP(timezone=False), server_onupdate=func.now(), nullable=True)

    id = Column(TEXT, primary_key=True, nullable=False)
    # created_utc = Column(TIMESTAMP(timezone=False), ullable=False)
    # updated_utc = Column(TIMESTAMP(timezone=False), nullable=True)
