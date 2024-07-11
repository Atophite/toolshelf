from textual.screen import ModalScreen, Screen
from textual.widgets import Label, Footer, OptionList
from textual.containers import Grid
from textual.binding import Binding


class ConfirmScreenModal(ModalScreen):

    BINDINGS = [
        Binding(key="ctrl+q", action="quit", description="Exit screen"),

    ]

    def action_quit(self):
        self.dismiss()

    def on_option_list_option_highlighted(self, option):
        pass
        
    def on_option_list_option_selected(self, option):
        pass

    def compose(self):
        yield Grid(
                Label("Are you sure you wanna do this?", id="question"),
                OptionList(
                    "Yes",
                    "No",
                ),
                id="dialog",
            )
        yield Footer()