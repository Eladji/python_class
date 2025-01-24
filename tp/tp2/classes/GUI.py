from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, TextView
from textual.containers import Horizontal, Vertical
# from classes.FleetManager import FleetManager
class GUI(App):
    BINDINGS = [("d", "toggle_dark", "activer le mode sombre"),]
        
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
    
    def dark_mode(self):
        self.theme = ("thetual-dark" if self.theme == "thetual-light" else "thetual-light")
    
if __name__ == "__main__":
    GUI = GUI()
    GUI.run()