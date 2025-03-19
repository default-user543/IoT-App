from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from confirm import ConfirmScreen  #  Import màn hình confirm
# Import các màn hình từ các file khác
from login import LoginImageScreen
from signin import SignInImageScreen
from forgotpass import ForgotPasswordScreen  #  Thêm màn hình Forgot Password

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

        # Tạo nút "Log in"
        login_button = Button(
            text="Log in",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            font_size='20sp',
            background_color=(0.6, 0.8, 1.0, 1.0),  # Màu #99CCFF
            background_normal='',
            background_down=''
        )

        # Tạo nút "Sign in"
        signin_button = Button(
            text="Sign in",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            font_size='20sp',
            background_color=(0.6, 0.8, 1.0, 1.0),
            background_normal='',
            background_down=''
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
        self.manager.current = 'login_image'

    def go_to_signin_image_screen(self, instance):
        self.manager.current = 'signin_image'

# Lớp chính của ứng dụng
class MyApp(App):
    def build(self):
        # Tạo ScreenManager để quản lý các màn hình
        screen_manager = ScreenManager()

        # Thêm màn hình chính
        screen_manager.add_widget(MainScreen(name='main'))

        # Thêm màn hình hình ảnh đăng nhập
        screen_manager.add_widget(LoginImageScreen(name='login_image'))

        # Thêm màn hình hình ảnh đăng ký
        screen_manager.add_widget(SignInImageScreen(name='signin_image'))

        # Thêm màn hình Forgot Password 
        screen_manager.add_widget(ForgotPasswordScreen(name='forgotpass'))
        screen_manager.add_widget(ConfirmScreen(name='confirm'))
        return screen_manager

if __name__ == "__main__":
    MyApp().run()
