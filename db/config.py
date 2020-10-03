from .database import SessionLocal
from typing import Union


def get_db() -> Union[SessionLocal, None]:
    db = SessionLocal()
    try:
        # yield db
        return db
    finally:
        db.close()
