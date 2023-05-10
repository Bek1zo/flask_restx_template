"""Core models."""

from sqlalchemy import Column, TEXT
from sqlalchemy.orm import relationship


from .model_base import BaseClass


class User(BaseClass):
    """Пользователи"""
    __tablename__ = 'users'
    # __table_args__ = {'schema': 'core', 'comment': 'Пользователи'}
    __table_args__ = {'comment': 'Пользователи'}

    name = Column(TEXT, unique=True, nullable=False, doc='Имя пользователя')

    def __repr__(self):
        return "{}".format(self.name)


class Data(BaseClass):
    """Информация"""
    __tablename__ = 'data'
    # __table_args__ = {'schema': 'core', 'comment': 'Информация'}
    __table_args__ = {'comment': 'Информация'}

    note = Column(TEXT, nullable=False, doc='Информация')

    def __repr__(self):
        return "{}".format(self.note)

