from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label

class ImageButton(ButtonBehavior, Image):
    pass

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        
        # Tạo layout
        layout = FloatLayout()
        
        username_label = Label(
            text = 'Username',
            size_hint = (None, None),
            size = (200, 50),
            pos_hint ={'x':0, 'top':1},
            font_size = 18,
            color = (1,1,1,1),
            halign = 'left'
        )
        layout.add_widget(username_label)

        # Tạo hình nền
        bg = Image(source='homescreen.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)
        
        # Tạo một hình ảnh có thể nhấn được (ImageButton)
        touch_area = ImageButton(
            source='homescreen.png',  # Bạn có thể thay bằng hình ảnh khác nếu muốn
            size_hint=(1, 1),
            allow_stretch=True,
            keep_ratio=False
        )
        touch_area.bind(on_press=self.go_to_menu)  # Gắn sự kiện khi chạm vào
        layout.add_widget(touch_area)
        
        # Thêm layout vào màn hình
        self.add_widget(layout)
    
    def go_to_menu(self, instance):
        self.manager.current = 'menu'  # Chuyển sang màn hình menu