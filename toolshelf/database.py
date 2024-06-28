
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

config_dir = os.path.expanduser('~/.config/toolshelf')
db_path = os.path.join(config_dir, 'toolshelf.db')
os.makedirs(config_dir, exist_ok=True)
DATABASE_URL = f'sqlite:///{db_path}'

# Create a new SQLite database (or connect to an existing one)
engine = create_engine(DATABASE_URL, echo=True)

# Base class for declarative class definitions
Base = declarative_base()

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

