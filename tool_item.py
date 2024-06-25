from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget
from textual.widgets import *
from textual.widgets.option_list import Option, Separator



class ToolItem():


    def __init__(self, name: str, description: str) -> None:
        self.tool_name = name
        self.tool_description = description
        super().__init__()
