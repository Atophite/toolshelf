from textual.app import App
from textual.widgets import *
from textual.screen import Screen, ModalScreen
from textual.containers import Grid
from textual.binding import Binding
from textual.widgets.option_list import Option
from textual.widgets import *
from toolshelf.models.tool_item import ToolItem
from toolshelf.managers.tool_manager import ToolManager as tm


class EditToolScreenModal(ModalScreen[ToolItem]):

    BINDINGS = [
        Binding(key="ctrl+q", action="quit", description="Exit screen"),
        Binding(key="ctrl+s", action="edit", description="Edit tool"),

    ]

    INPUTS: list[Input] = [
        Input(placeholder="Tool name", max_length=15, id="name"),
        Input(placeholder="Description", max_length=100, id="description"),
        Input(placeholder="Command", max_length=50, id="command")
    ]

    def __init__(self, tool: ToolItem, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tool = tool
        self.INPUTS: list[Input] = [
            Input(value=tool.name, placeholder="Tool name", max_length=15, id="name"),
            Input(value=tool.description, placeholder="Description", max_length=100, id="description"),
            Input(value=tool.command, placeholder="Command", max_length=50, id="command")
        ]

    def reset_state(self):
        for input_field in self.INPUTS:
            input_field.value = ""
        self.INPUTS[0].focus()

    def action_quit(self):
        self.dismiss()

    def action_edit(self):
        tool = ToolItem(self.INPUTS[0].value, self.INPUTS[1].value, self.INPUTS[2].value)

        self.dismiss(tool)
        

    def compose(self):
    
        yield Grid(
                Label(f"Edit tool {self.tool.name}", id="question"),
                *self.INPUTS,
                id="dialog",
            )
        yield Footer()