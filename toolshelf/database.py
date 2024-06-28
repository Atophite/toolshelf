
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a new SQLite database (or connect to an existing one)
engine = create_engine('sqlite:///toolshelf.db', echo=True)

# Base class for declarative class definitions
Base = declarative_base()

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

