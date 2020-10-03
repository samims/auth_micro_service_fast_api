from logging.config import fileConfig
from pathlib import Path

from sqlalchemy import engine_from_config
from sqlalchemy import pool

import os, sys
from dotenv import load_dotenv

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
folder = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(folder))

# load_dotenv(os.path.join(BASE_DIRDIR, ".env"))

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
# sqlalchemy.url = postgresql://sse002@localhost:5432/learn
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


AUTH_DB_DRIVER = os.environ["AUTH_DB_DRIVER"]
AUTH_DB_HOST = os.environ["AUTH_DB_HOST"]
AUTH_DB_PORT = os.environ["AUTH_DB_PORT"]
AUTH_DB_NAME = os.environ["AUTH_DB_NAME"]
AUTH_DB_USER = os.environ["AUTH_DB_USER"]
AUTH_DB_PASS = os.environ["AUTH_DB_PASS"]

AUTH_DB_URL = f"{AUTH_DB_DRIVER}://{AUTH_DB_USER}:{AUTH_DB_PASS}@{AUTH_DB_HOST}:{AUTH_DB_PORT}/{AUTH_DB_NAME}"

config.set_main_option("sqlalchemy.url", AUTH_DB_URL)
# to set env var for db to alembic.ini
# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from db.database import Base
from db.models.user import User

target_metadata = Base.metadata


# target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
