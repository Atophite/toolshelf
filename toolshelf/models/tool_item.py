from database import engine, Base
from sqlalchemy import Column, Integer, String, Boolean

class ToolItem(Base):
    __tablename__ = 'tools'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    command = Column(String)
    installed = Column(Boolean)

    def __init__(self, name: str, description: str, command: str, installed: bool) -> None:
        self.name = name
        self.description = description
        self.command = command
        self.installed = installed






# Create the table in the database
Base.metadata.create_all(engine)

