from toolshelf.exceptions import InvalidToolException
from toolshelf.models.tool_item import ToolItem
from sqlalchemy import Column, Integer, String, Boolean, select, update
from toolshelf.database import session
import subprocess

class ToolManager:
    @staticmethod
    def add_tool(toolItem: "ToolItem"):

        if len(toolItem.name) >= 1:
            session.add(toolItem)
            session.commit()
        else:
            raise InvalidToolException("Tool name can't be empty!")


    @staticmethod
    def delete_tool(toolItemId: int) -> None:
        session.delete(ToolManager.get_tool(toolItemId))
        session.commit()

    @staticmethod
    def edit_tool(toolItemId: int, tool: ToolItem):
        session.execute(
            update(ToolItem).where(ToolItem.id == toolItemId)
                .values(
                    name= tool.name,
                    description = tool.description,
                    command = tool.command,
                )
        )
        session.commit()
    

    @staticmethod
    def get_tools():
        toolItems = session.query(ToolItem).all()

        toolItems_sorted = sorted(toolItems, key=lambda x: x.name, reverse=False)
        return toolItems_sorted
    

    @staticmethod
    def get_tool(toolItemId: int) -> "ToolItem":
        statement = select(ToolItem).filter_by(id=toolItemId)
        
        return session.get_one(ToolItem, toolItemId)

    @staticmethod
    def get_installed(tool: "ToolItem") -> bool:
        try:
            result = subprocess.run(['which', tool.command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.returncode == 0
        except FileNotFoundError:
            return False
        
    @staticmethod
    def get_tool_color(tool: "ToolItem") -> str:
        if ToolManager.get_installed(tool):
            return "[green]" + tool.name
        else:
            return "[red]" + tool.name
