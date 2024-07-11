from textual.widget import Widget
from textual.widgets import Static, Label


class ToolDescLabelWidget(Static):

    type: str
    desc: str

    def __init__(self, type, desc):
        self.type = type
        self.desc = desc
        super().__init__()

    def compose(self):
        yield Label(self.type, id="type")
        yield Label(self.desc, id="description")
