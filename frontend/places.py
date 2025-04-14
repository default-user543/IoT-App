from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window

class PlacesScreen(Screen):
    def __init__(self, **kwargs):
        super(PlacesScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        layout.add_widget(Label(text="Welcome to Places Screen", pos_hint={"center_x": 0.5, "center_y": 0.5}))
        self.add_widget(layout)