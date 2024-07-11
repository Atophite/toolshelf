from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Label, Static, TextArea
from textual.containers import Horizontal, VerticalScroll
from toolshelf.models.tool_item import ToolItem
from textual.reactive import reactive
from rich.table import Table
from toolshelf.widgets import ToolDescLabelWidget



class ToolDescriptionScreen(Widget):

    toolItem: ToolItem = reactive(ToolItem())
    # text_area = TextArea.code_editor(toolItem.name, language="markdown", read_only=True, show_line_numbers=False)
    
    CSS_PATH = [
        "styling/tool_description.tcss",
    ]

    def compose(self):
        yield Label("name:", classes="tooltype")
        yield Label("\n", id='name', classes="tooldescription")

        yield Label("description:", classes="tooltype")
        yield Label("", id="description", classes="tooldescription")

        yield Label("command:", classes="tooltype")
        yield Label("", id="command", classes="tooldescription")

        yield Label("installed:", classes="tooltype")
        yield Label("", id="installed", classes="tooldescription")



    def watch_toolItem(self, toolItem: ToolItem):
        self.get_widget_by_id(id='name').update(self.toolItem.name)
        self.get_widget_by_id(id='description').update(self.toolItem.description)
        self.get_widget_by_id(id="command").update(self.toolItem.command)

        if(self.toolItem.installed):
            self.get_widget_by_id(id='installed').update(str("✅"))
        else:
            self.get_widget_by_id(id='installed').update(str("❌"))





