from toolshelf.models.tool_item import ToolItem
from sqlalchemy import Column, Integer, String, Boolean, select, update
from toolshelf.database import session
import subprocess

class ToolManager:
    @staticmethod
    def add_tool(toolItem: "ToolItem"):
        new_tool = toolItem
        session.add(new_tool)
        session.commit()

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
        return session.query(ToolItem).all()
    

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
