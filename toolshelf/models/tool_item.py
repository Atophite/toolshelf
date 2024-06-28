from toolshelf.database import *

class ToolItem(Base):
    __tablename__ = 'tools'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description






# Create the table in the database
Base.metadata.create_all(engine)

