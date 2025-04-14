from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

        layout = FloatLayout()
        self.bg = Image(source='menu.png', keep_ratio=False, allow_stretch=True)
        layout.add_widget(self.bg)
    
        # Share button
        self.sharebutton = Button(
            text='[b]Share your destination[/b]',
            markup=True,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            background_normal='',
            background_color=(0.2, 0.6, 1, 1)
        )
        self.sharebutton.bind(on_press=self.go_to_share_screen)
        layout.add_widget(self.sharebutton)

        # Back button
        self.backbutton = Button(
            text='Back',
            size_hint=(None, None),
            size=(100, 50), 
            pos_hint={'center_x': 0.1, 'center_y': 0.9},
            background_normal='',
            background_color=(0.2, 0.6, 1, 1)
        )
        self.backbutton.bind(on_press=self.go_back_to_home)
        layout.add_widget(self.backbutton)

        # Places button
        self.placebutton = Button(
            text='[b]Places Information[/b]',
            markup=True,
            size_hint=(None, None),
            size=(200, 50), 
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            background_normal='',
            background_color=(0.2, 0.6, 1, 1)
        )
        self.placebutton.bind(on_press=self.go_to_places_screen)
        layout.add_widget(self.placebutton)

        self.add_widget(layout)
    
    def go_back_to_home(self, instance):
        self.manager.current = 'home'

    def go_to_share_screen(self, instance):
        self.manager.current = 'share'

    def go_to_places_screen(self, instance):
        self.manager.current = 'places'

class PlacesScreen(Screen):
    def __init__(self, **kwargs):
        super(PlacesScreen, self).__init__(**kwargs)

        layout = FloatLayout()
        self.bg = Image(source='places.png', keep_ratio=False, allow_stretch=True)
        layout.add_widget(self.bg)

        # Back button
        self.backbutton = Button(
            text='Back',
            size_hint=(None, None),
            size=(100, 50), 
            pos_hint={'center_x': 0.1, 'center_y': 0.9},
            background_normal='',
            background_color=(0.2, 0.6, 1, 1)
        )
        self.backbutton.bind(on_press=self.go_back_to_menu)
        layout.add_widget(self.backbutton)

        self.add_widget(layout)
    
    def go_back_to_menu(self, instance):
        self.manager.current = 'menu'
