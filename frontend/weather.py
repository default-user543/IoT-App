from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

class WeatherScreen(Screen):
    def __init__(self, **kwargs):
        super(WeatherScreen, self).__init__(**kwargs)
        
        # Tạo layout
        layout = FloatLayout()
        
        # Thêm hình nền cho màn hình Weather
        bg = Image(source='Weather.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)

        back_button1 = Button(
        text = "Back",
        size_hint = (None, None),
        size = (100,50),
        pos_hint = {'x':0.2, 'right':0,5},
        background_color = (0,0,0,0),
        color = (1,1,1,1),
        font_size = 18
        )
        back_button1.bind(on_press = self.go_back)
        layout.add_widget(back_button1)
        
        # Thêm layout vào màn hình
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = 'home'