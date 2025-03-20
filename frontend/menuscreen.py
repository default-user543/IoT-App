from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
        # Tạo layout
        layout = FloatLayout()
        
        # Thêm hình nền cho menu
        bg = Image(source='menu screen.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)
        
        # Tạo nút Weather
        weather_button = Button(
            text="Weather",
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.45},
            background_color=(0.2, 0.6, 1, 1),  # Màu nền
            color=(1, 1, 1, 1)  # Màu chữ
        )
        weather_button.bind(on_press=self.go_to_weather)
        layout.add_widget(weather_button)
        
        # Tạo nút GPS
        gps_button = Button(
            text="GPS",
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.25},
            background_color=(0.2, 0.6, 1, 1),  # Màu nền
            color=(1, 1, 1, 1)  # Màu chữ
        )
        gps_button.bind(on_press=self.go_to_gps)
        layout.add_widget(gps_button)
        
        # Thêm layout vào màn hình
        self.add_widget(layout)
    
    def go_to_weather(self, instance):
        self.manager.current = 'weather'  # Chuyển sang màn hình Weather
    
    def go_to_gps(self, instance):
        self.manager.current = 'gps'  # Chuyển sang màn hình GPS