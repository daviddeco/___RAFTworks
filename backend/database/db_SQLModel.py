"""database itself template call"""

### db.py
from sqlmodel import SQLModel, create_engine, Session

engine = create_engine("sqlite:///data/pos_demo.db", echo=True)


def init_db():
    from ..models import sales_model

    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
