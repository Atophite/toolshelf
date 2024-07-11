from toolshelf.database import engine, Base
from sqlalchemy import Column, Integer, String, Boolean, select
from toolshelf.database import session
import subprocess

def add_tool(toolItem: "ToolItem"):
    new_tool = toolItem
    session.add(new_tool)
    session.commit()

def delete_tool(toolItemId: int) -> None:
    session.delete(get_tool(toolItemId))
    session.commit()
        
def get_tools():
    return session.query(ToolItem).all()

def get_tool(toolItemId: int) -> "ToolItem":
    statement = select(ToolItem).filter_by(id=toolItemId)
    
    return session.get_one(ToolItem, toolItemId)


def get_installed(tool: "ToolItem") -> bool:
    try:
        result = subprocess.run(['which', tool.command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def get_tool_color(tool: "ToolItem") -> str:
    if get_installed(tool):
        return "[green]" + tool.name
    else:
        return "[red]" + tool.name

    

class ToolItem(Base):
    __tablename__ = 'tools'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    command = Column(String)
    installed = Column(Boolean)

    def __init__(self, name: str="", description: str="", command: str="", installed: bool=False):
        self.name = name
        self.description = description
        self.command = command
        self.installed = installed

    




# Create the table in the database
Base.metadata.create_all(engine)

