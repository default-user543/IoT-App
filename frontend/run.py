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

# Gọi lại hàm
from main import MainScreen
from login import LoginScreen
from login import LoginImageScreen
from signin import SignInScreen
from signin import SignInImageScreen

# Lớp chính của ứng dụng
class MyApp(App):
    def build(self):
        # Tạo ScreenManager để quản lý các màn hình
        screen_manager = ScreenManager()

        # Thêm màn hình chính
        main_screen = MainScreen(name='main')
        screen_manager.add_widget(main_screen)

        # Thêm màn hình hình ảnh đăng nhập
        login_image_screen = LoginImageScreen(name='login_image')
        screen_manager.add_widget(login_image_screen)

        # Thêm màn hình hình ảnh đăng ký
        signin_image_screen = SignInImageScreen(name='signin_image')
        screen_manager.add_widget(signin_image_screen)

        # Thêm màn hình đăng nhập
        login_screen = LoginScreen(name='login')
        screen_manager.add_widget(login_screen)

        # Thêm màn hình đăng ký
        signin_screen = SignInScreen(name='signin')
        screen_manager.add_widget(signin_screen)

        return screen_manager

if __name__ == "__main__":
    app = MyApp()
    app.run()
