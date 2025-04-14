from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.label import Label
from kivy.uix.button import Button, ButtonBehavior

class TouchableImage(ButtonBehavior, Image):
    pass

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        
        # Tạo layout chính
        layout = FloatLayout()
        
        # Tải ảnh nền và xác định kích thước
        self.bg = Image(source='homescreen.png', keep_ratio=False, allow_stretch=True)
        layout.add_widget(self.bg)
        
        # Tạo vùng chạm toàn màn hình
        self.touch_area = TouchableImage(
            source='homescreen.png',
            size_hint=(1, 1),
            keep_ratio=False,
            allow_stretch=True
        )
        self.touch_area.bind(on_press=self.go_to_menu_screen)
        self.add_widget(layout)

        #tạo nút back để trở về trang main.py:
        self.backbutton = Button(
            text='Sign out',
            size_hint=(None, None),
            size=(100, 50), 
            pos_hint={'right': 1, 'top': 1},
            background_normal='',
            background_color=(0.2, 0.6, 1, 1)
        )
        self.backbutton.bind(on_press=self.go_back_to_main)
        
        #điều chỉnh kích thước dựa trên nền tảng:
        if platform != ['android', 'ios']:
            self.set_window_size()
    

    #thêm các nút bấm theo thứ tự:
        layout.add_widget(self.touch_area)
        layout.add_widget(self.backbutton)
    
    
    # định nghĩa thao tác:
    def go_to_menu_screen(self, instance):
        self.manager.current = 'menu' #đi đến menuscreen.py
    
    def go_back_to_main(self, instance):
        self.manager.current = 'main' #đi đến main.py
    
    # Thay đổi kích thước cửa sổ ứng dụng trên máy tính
    def set_window_size(self):
        from kivy.core.image import Image as CoreImage
        img = CoreImage('homescreen.png')
        width, height = img.size
        Window.size = (width*0.35, height*0.35)   
    
    

