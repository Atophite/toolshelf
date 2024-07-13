from toolshelf.database import engine, Base
from sqlalchemy import Column, Integer, String, Boolean, select


class ToolItem(Base):
    __tablename__ = 'tools'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    command = Column(String)

    def __init__(self, name: str="", description: str="", command: str=""):
        self.name = name
        self.description = description
        self.command = command

    

# Create the table in the database
Base.metadata.create_all(engine)

