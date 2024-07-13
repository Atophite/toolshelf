from textual.screen import ModalScreen, Screen
from textual.widgets import Label, Footer, OptionList, Button
from textual.containers import Grid
from textual.binding import Binding


class ConfirmScreenModal(ModalScreen[bool]):

    BINDINGS = [
        Binding(key="ctrl+q", action="quit", description="Exit screen"),
        Binding(key="right", action="right", description="right", show=False),
        Binding(key="left", action="left", description="left", show=False)

    ]

    def action_right(self):
        self.app.action_focus_next()
        
    def action_left(self):
        self.app.action_focus_previous()

    def on_button_pressed(self, event: Button.Pressed):
        if(event.button.id == "yes"):
            self.dismiss(True)
        else:
            self.dismiss(False)

    def action_quit(self):
        self.dismiss(False)

    def compose(self):
        yield Grid(
                Label("Are you sure you want to delete?", id="question"),
                Grid(
                Button("yes", variant="success", id="yes"),
                Button("no", variant="error", id="no"),
                    classes="button-grid"
                ),
                id="dialog",
            )
        yield Footer()