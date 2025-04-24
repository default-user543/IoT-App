from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

# Thiết lập màu nền cho ứng dụng
Window.clearcolor = (1, 1, 1, 1)  # Màu trắng

# Màn hình chính
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Tạo layout chính với FloatLayout
        layout = FloatLayout()

        # Tạo widget Image để hiển thị ảnh nền
        background = Image(source='background.png', allow_stretch=True, keep_ratio=False, size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})

        #Xì tai cho mấy em nút
        class RoundedButton(Button):
            def __init__(self, **kwargs):
                super(RoundedButton, self).__init__(**kwargs)
                self.background_normal = ''
                self.background_down = ''
                self.background_color = (0, 0, 0, 0)  # Làm trong suốt để dùng canvas vẽ
                self.color = (1, 1, 1, 1)  # Màu chữ

                with self.canvas.before:
                    Color(0.6, 0.8, 1.0, 1.0)  # Màu nền #99CCFF
                    self.rect = RoundedRectangle(radius=[20])

                self.bind(pos=self.update_rect, size=self.update_rect)

            def update_rect(self, *args):
                self.rect.pos = self.pos
                self.rect.size = self.size


        # Tạo nút "Log in" với màu nút #99CCFF
        login_button = RoundedButton(
            text="Log in",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            font_size='20sp',  # Phóng to chữ
        )

        # Tạo nút "Sign in" với màu nút #99CCFF
        signin_button = RoundedButton(
            text="Sign in",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            font_size='20sp',  # Phóng to chữ
        )

        # Thêm sự kiện khi nhấp vào nút "Log in"
        login_button.bind(on_press=self.go_to_login_image_screen)

        # Thêm sự kiện khi nhấp vào nút "Sign in"
        signin_button.bind(on_press=self.go_to_signin_image_screen)

        # Thêm các widget vào layout
        layout.add_widget(background)
        layout.add_widget(login_button)
        layout.add_widget(signin_button)

        # Thêm layout vào màn hình
        self.add_widget(layout)

    def go_to_login_image_screen(self, instance):
        # Chuyển sang màn hình hình ảnh đăng nhập
        self.manager.current = 'login_image'

    def go_to_signin_image_screen(self, instance):
        # Chuyển sang màn hình hình ảnh đăng ký
        self.manager.current = 'signin_image'

