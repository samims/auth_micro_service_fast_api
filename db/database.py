import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://sse002@localhost:5432/learn"

auth_db_driver = os.environ["AUTH_DB_DRIVER"]
auth_db_host = os.environ["AUTH_DB_HOST"]
auth_db_port = os.environ["AUTH_DB_PORT"]
auth_db_name = os.environ["AUTH_DB_NAME"]
auth_db_user = os.environ["AUTH_DB_USER"]
auth_db_pass = os.environ["AUTH_DB_PASS"]

SQLALCHEMY_DATABASE_URL = f"{auth_db_driver}://{auth_db_user}:{auth_db_pass}@{auth_db_host}:{auth_db_port}/{auth_db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
