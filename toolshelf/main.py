from textual.app import App, ComposeResult
from textual.widgets.option_list import Option
from textual.widgets import *
from textual.screen import Screen, ModalScreen
from textual.containers import Grid
from textual.binding import Binding
from textual.logging import TextualHandler
from textual import events
from rich.table import Table
from toolshelf.models.tool_item import ToolItem
from toolshelf.database import session
from toolshelf.screens import ToolScreenModal, ToolDescriptionScreen, ConfirmScreenModal, EditToolScreenModal
from toolshelf.managers.tool_manager import ToolManager as tm

import pyperclip
import logging
import subprocess

logging.basicConfig(
    level="ERROR",
    handlers=[TextualHandler()],
)

class ToolShelfApp(App):

    selected_option: Option = None

    option_list = OptionList(*[Option(tm.get_tool_color(tool), id=tool.id) for tool in tm.get_tools()], classes="sidebar")

    SCREENS = {
        "toolModal": lambda: ToolScreenModal(classes="modal"),
        "confirmModal": lambda: ConfirmScreenModal(classes="modal")
    }

    
    CSS_PATH = [
        "styling/dock_sidebar.tcss",
        "styling/create_tool_modal.tcss",
        "styling/tool_description.tcss"
    ]

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit", priority=True),
        Binding(key="c", action="create", description="Create"),
        Binding(key="delete", action="delete", description="Delete"),
        Binding(key="p", action="copy", description="Copy"),
        Binding(key="e", action="edit", description="Edit"),
        Binding(key="l", action="focus", description="Change panel"),
    ]

    #----------------------ACTIONS-------------------------------------------
    def action_focus(self):
        self.app.action_focus_next()

    def action_create(self):
        self.push_screen("toolModal", self.create_tool)

    def action_delete(self):
        try:
            self.push_screen("confirmModal", self.delete_tool)
        except:
            pass
    
    def action_edit(self):
        self.push_screen(EditToolScreenModal(tool=tm.get_tool(self.selected_option.option_id), classes="modal"), self.edit_tool)

    def action_copy(self):
        toolItem: ToolItem = tm.get_tool(self.selected_option.option_id)
        pyperclip.copy(toolItem.command)

    #--------------------------METHODS----------------------------------------
    def create_tool(self, tool: ToolItem):
        tm.add_tool(tool)
        self.option_list.add_option(Option(tm.get_tool_color(tool), id=tool.id))
    
    def edit_tool(self, tool: ToolItem):
        tm.edit_tool(toolItemId=self.selected_option.option_id, tool=tool)
        self.option_list.replace_option_prompt(self.selected_option.option_id, tm.get_tool_color(tool))
        self.query_one(ToolDescriptionScreen).toolItem = tool

    def delete_tool(self, delete: bool):
            if(delete):
                try:
                    
                    tm.delete_tool(toolItemId=self.selected_option.option_id)
                    self.option_list.remove_option(option_id=self.selected_option.option_id)
                    self.notify("Tool deleted!")
                except:
                    self.notify("Cannot delete tool!", severity="error")


    #---------------------------EVENTS------------------------------------
    def on_option_list_option_highlighted(self, option):
        self.selected_option = option
        # self.log(self.query_one(ToolDescriptionScreen).toolItem)
        
        self.log(tm.get_tool(option.option_id))
        self.query_one(ToolDescriptionScreen).toolItem = tm.get_tool(option.option_id)
        
    def on_option_list_option_selected(self, option):
        # option = OptionSelected
        with self.suspend():
            tool: ToolItem = tm.get_tool(option.option_id)
            self.log(tool.name)  
            subprocess.call([tool.command])

    #-----------------------------_COMPOSE-------------------------
    def compose(self) -> ComposeResult:
        yield self.option_list
        yield ToolDescriptionScreen(id="description")
        yield Footer()
    
app = ToolShelfApp().run()

# if __name__ == "__main__":
#     app = ToolShelfApp()
#     app.run(mouse= True)