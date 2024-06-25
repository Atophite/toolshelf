from textual.app import App, ComposeResult
from textual.widgets import *
from tool_item import *
from textual.binding import Binding
from textual.logging import TextualHandler
from textual import events
from rich.table import Table
import logging
import subprocess

logging.basicConfig(
    level="INFO",
    handlers=[TextualHandler()],
)

LIST: list = [ToolItem("spotify_player", "A spotify player"),ToolItem("sdf", "sdf")]

class Main(App):
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

    def action_create(self):
        self.log("CREATEEE")

    def on_load(self):
        self.log("sdfsfd")


    def compose(self) -> ComposeResult:
        yield OptionList(*[Option(item.tool_name) for item in LIST], id="sidebar")
        yield Footer()

    def on_option_list_option_selected(self, option):
        with self.suspend():  
            subprocess.call(["spotify_player"])
            self.log(LIST[option.option_index])


if __name__ == "__main__":
    app = Main()
    app.run(mouse= False)