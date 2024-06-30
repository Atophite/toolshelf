from textual.app import App, ComposeResult
from textual.widgets.option_list import Option
from textual.widgets import *
from textual.screen import Screen, ModalScreen
from textual.containers import Grid
from models.tool_item import *
from textual.binding import Binding
from textual.logging import TextualHandler
from textual import events
from rich.table import Table
from database import session
import logging
import subprocess



logging.basicConfig(
    level="ERROR",
    handlers=[TextualHandler()],
)


def add_tool(toolItem: ToolItem):
    new_tool = toolItem
    session.add(new_tool)
    session.commit()


def get_tools():
    return session.query(ToolItem).all()

def get_tool(toolItemId: int) -> ToolItem:
    return session.query(ToolItem).filter_by(id=toolItemId).first()

option_list: OptionList = OptionList(*[Option(item.name, id=item.id) for item in get_tools()], id="tool_list")



class ToolShelfApp(App):
    print("test")

    SCREENS = {
        "toolModal": lambda: ToolScreenModal(id="modal")
    }

    
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
        Binding("enter", "select_cursor", "Select", show=True),
        Binding("up", "cursor_up", "Cursor Up", show=True),
        Binding("down", "cursor_down", "Cursor Down", show=True),
    ]


    def action_create(self):
        self.push_screen("toolModal")
        # tool = ToolItem("spotify_player", "A spotify player", "spotify_player", True)
        # add_tool(tool)
        # self.option_list.add_option(Option(tool.name))

        # tool = ToolItem("lazydocker", "Docker lazy", "lazydocker", True)
        # add_tool(tool)
        # self.option_list.add_option(Option(tool.name))

    def on_load(self):
        self.log("sdfsfd")


    def compose(self) -> ComposeResult:
        yield option_list
        yield Footer()
        

    def on_option_list_option_selected(self, option):
        # option = OptionSelected
        with self.suspend():
            tool: ToolItem = get_tool(option.option_id)
            self.log(tool.name)  
            subprocess.call([tool.command])

class ToolScreenModal(ModalScreen):
    BINDINGS = [
        Binding(key="ctrl+q", action="quit", description="Exit screen"),
        Binding(key="ctrl+s", action="create", description="Create tool"),

    ]

    INPUTS: list[Input] = [
        Input(placeholder="Tool name", max_length=15, id="name"),
        Input(placeholder="Description", max_length=50, id="description"),
        Input(placeholder="Command", max_length=50, id="command")
    ]

    def reset_state(self):
        for input_field in self.INPUTS:
            input_field.value = ""
        self.INPUTS[0].focus()

    def action_quit(self):
        self.reset_state()
        self.dismiss(False)

    def action_create(self):
        tool = ToolItem(self.INPUTS[0].value, self.INPUTS[1].value, self.INPUTS[2].value, True)
        add_tool(tool)
        option_list.add_option(Option(tool.name))
        self.reset_state()
        self.dismiss(False)

    # def action_cursor_down(self):
    #     if(self.cursor <= len(self.INPUTS)):
    #         self.cursor += 1
    #         self.INPUTS[self.cursor].focus()
    
    # def action_cursor_up(self):
    #     if(self.cursor >= 0):
    #         self.cursor -= 1
    #         self.INPUTS[self.cursor].focus()
        

    def compose(self):
    
        yield Grid(
                Label("Add a new tool", id="question"),
                *self.INPUTS,
                id="dialog",
            )
        yield Footer()

def main():
    ToolShelfApp().run(mouse=False)

if __name__ == "__main__":
    app = ToolShelfApp()
    app.run(mouse= True)