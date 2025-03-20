from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

class GPSScreen(Screen):
    def __init__(self, **kwargs):
        super(GPSScreen, self).__init__(**kwargs)
        
        # Tạo layout
        layout = FloatLayout()
        
        # Thêm hình nền cho màn hình GPS
        bg = Image(source='GPS screen.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)
        
        # Thêm một label hoặc các widget khác
        label = Label(
            text="GPS Information",
            font_size=24,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.add_widget(label)
        
        # Thêm layout vào màn hình
        self.add_widget(layout)