"""Session."""
import os
from contextlib import contextmanager

from flask import current_app, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.orm.session import Session as SessionSQLA

Session = sessionmaker()

@contextmanager
def session_scope(session: SessionSQLA = Session) -> SessionSQLA:
    """Provide a transactional scope around a series of operations."""
    if 'FLASK_DEBUG' in os.environ:
        db_uri = current_app.config.get('DB_URI', '')
        echo = True
    else:
        db_uri = current_app.config.get('DB_URI', '').format(request.environ['REMOTE_USER'])
        echo = False
    # session.configure(bind=create_engine(db_uri, client_encoding='utf8', poolclass=NullPool, echo=echo)) # для postgresql
    session.configure(bind=create_engine(db_uri, poolclass=NullPool, echo=echo)) # для sqlite

    sess = session()
    try:
        yield sess
        sess.commit()
    except:
        sess.rollback()
        raise
    finally:
        sess.close()
        # sess.invalidate()
