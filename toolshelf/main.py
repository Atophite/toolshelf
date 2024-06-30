from textual.app import App, ComposeResult
from textual.widgets.option_list import Option
from textual.widgets import *
from textual.screen import Screen, ModalScreen
from textual.containers import Grid
from toolshelf.models.tool_item import ToolItem
from textual.binding import Binding
from textual.logging import TextualHandler
from textual import events
from rich.table import Table
from toolshelf.database import session
from toolshelf.screens.create_tool_modal import ToolScreenModal
from toolshelf.models.tool_item import get_tool, get_tools, add_tool, delete_tool

import logging
import subprocess



logging.basicConfig(
    level="ERROR",
    handlers=[TextualHandler()],
)





class ToolShelfApp(App):

    selected_option: Option

    option_list = OptionList(*[Option(tool.name, id=tool.id) for tool in get_tools()], id="sidebar")

    SCREENS = {
        "toolModal": lambda: ToolScreenModal(id="modal")
    }

    
    CSS_PATH = [
        "styling/dock_sidebar.tcss",
        "styling/create_tool_modal.tcss"
    ]

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="c", action="create", description="Create new"),
        Binding(key="delete", action="delete", description="Delete tool"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding("enter", "select_cursor", "Select", show=True),
        Binding("up", "cursor_up", "Cursor Up", show=True),
        Binding("down", "cursor_down", "Cursor Down", show=True),
    ]

    def create_tool(self, tool: ToolItem):
        add_tool(tool)
        self.option_list.add_option(Option(tool.name, id=tool.id))
        

    def action_create(self):
        self.push_screen("toolModal", self.create_tool)

    def action_delete(self):
        try:
            delete_tool(toolItemId=self.selected_option.option_id)
            self.option_list.remove_option(option_id=self.selected_option_option_id)
        except:
            None


    def on_load(self):
        self.log("sdfsfd")

    def compose(self) -> ComposeResult:
        yield self.option_list
        yield Footer(Label("sdf"))

    def on_option_list_option_highlighted(self, option):
        self.selected_option = option
        
    def on_option_list_option_selected(self, option):
        # option = OptionSelected
        with self.suspend():
            tool: ToolItem = get_tool(option.option_id)
            self.log(tool.name)  
            subprocess.call([tool.command])
    




app = ToolShelfApp().run()

# if __name__ == "__main__":
#     app = ToolShelfApp()
#     app.run(mouse= True)