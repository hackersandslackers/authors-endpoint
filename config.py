"""Bot configuration variables."""
import os

# DB vars
database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
database_name = os.environ.get('SQLALCHEMY_DATABASE_NAME')
database_table = os.environ.get('SQLALCHEMY_TABLE')
database_schema = os.environ.get('SQLALCHEMY_DB_SCHEMA')
