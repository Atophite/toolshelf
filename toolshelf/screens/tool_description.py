from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Label, Static, TextArea
from textual.containers import Horizontal, VerticalScroll
from toolshelf.models.tool_item import ToolItem
from textual.reactive import reactive
from rich.table import Table
from toolshelf.widgets import ToolDescLabelWidget
from toolshelf.managers.tool_manager import ToolManager as tm
from textual.containers import ScrollableContainer



class ToolDescriptionScreen(ScrollableContainer):

    toolItem: ToolItem = reactive(ToolItem())
    # text_area = TextArea.code_editor(toolItem.name, language="markdown", read_only=True, show_line_numbers=False)
    
    CSS_PATH = [
        "styling/tool_description.tcss",
    ]

    def compose(self):
        yield Label("name:", classes="tooltype")
        yield Label("", id='name', classes="tooldescription")

        yield Label("description:", classes="tooltype")
        yield TextArea("empty...", id="description", read_only=True, disabled=True)

        yield Label("command:", classes="tooltype")
        yield Label("", id="command", classes="tooldescription")

        yield Label("installed:", classes="tooltype")
        yield Label("", id="installed", classes="tooldescription")




    def watch_toolItem(self, toolItem: ToolItem):
        self.get_widget_by_id(id='name').update(self.toolItem.name)
        if(self.toolItem.description is not ""):
            self.get_widget_by_id(id='description').text = self.toolItem.description
        else:
            self.get_widget_by_id(id='description').text = "empty"
        self.get_widget_by_id(id="command").update(self.toolItem.command)

        if(tm.get_installed(toolItem)):
            self.get_widget_by_id(id='installed').update(str("✅"))
        else:
            self.get_widget_by_id(id='installed').update(str("❌"))





