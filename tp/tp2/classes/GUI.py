from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button
from textual.containers import HorizontalGroup, VerticalGroup
from classes.FleetManager import FleetManager
from textual.reactive import reactive
# from classes.FleetManager import FleetManager
fleet_manager = FleetManager()
fleet_manager.load_data("component/save/")

# class shipui(VerticalGroup):
#     def compose(self):
#         for i in fleet_manager.get_current_fleet()._spaceship:
#             yield Button(label =i._name, action= self.on_button_press()) 
        
#     def on_button_press(self, button):
#         fleet_manager.set_current_ship(button.text)
#         self.app.title = fleet_manager.get_current_ship()._name
#         self.app.refresh()
class Fleetui(VerticalGroup):
    
    def compose(self):
        for i in fleet_manager._party:
            yield Button(label=i._name, id=i._name)
    
    def on_button_pressed(self, event: Button.Pressed):
        fleet_manager.change_fleet(event.button.id)
        
        self.app.sub_title=fleet_manager.get_current_fleet()._name
        self.refresh()
        
        
class GUI(App):
    
    BINDINGS = [("d", "toggle_dark", "activer le mode sombre"),]
    title = reactive("Fleet Manager")
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield HorizontalGroup(Fleetui())
    
    def on_mount(self):
        self.title = "Fleet Manager"
        self.sub_title = fleet_manager.get_current_fleet()._name
        
    
    
    
    def dark_mode(self):
        self.theme = ("thetual-dark" if self.theme == "thetual-light" else "thetual-light")

if __name__ == "__main__":
    GUI = GUI()
    GUI.run()