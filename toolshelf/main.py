from textual.app import App, ComposeResult
from textual.widgets.option_list import Option, Separator
from textual.widgets import *
from toolshelf.models.tool_item import *
from textual.binding import Binding
from textual.logging import TextualHandler
from textual import events
from rich.table import Table
import logging
import subprocess



logging.basicConfig(
    level="ERROR",
    handlers=[TextualHandler()],
)


def add_tool(name: str, description: str):
    new_tool = ToolItem(name=name, description=description)
    session.add(new_tool)
    session.commit()


def get_tools():
    return session.query(ToolItem).all()


class ToolShelfApp(App):
    print("KANKER")
    
    CSS_PATH = "styling/dock_sidebar.tcss"

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="c", action="create", description="Create new"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding("enter", "select_cursor", "Select", show=True, key_display="S"),
        Binding("up", "cursor_up", "Cursor Up", show=True),
        Binding("down", "cursor_down", "Cursor Down", show=True),
    ]

    option_list: OptionList = OptionList(*[Option(item.name) for item in get_tools()], id="sidebar")

    def action_create(self):
        tool = ToolItem("create test", "test desc")
        add_tool("create test", "test desc")
        self.option_list.add_option(Option(tool.name))

    def on_load(self):
        self.log("sdfsfd")


    def compose(self) -> ComposeResult:
        yield self.option_list
        yield Footer()

    def on_option_list_option_selected(self, option):
        with self.suspend():  
            subprocess.call(["spotify_player"])
            self.log(get_tools()[option.option_index])

def main():
    ToolShelfApp().run(mouse=False)

if __name__ == "__main__":
    app = ToolShelfApp()
    app.run(mouse= False)