from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
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

        # Tạo nút "Log in" với màu nút #99CCFF
        login_button = Button(
            text="Log in",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            font_size='20sp',  # Phóng to chữ
            background_color=(0.6, 0.8, 1.0, 1.0),  # Màu #99CCFF
            background_normal='',  # Loại bỏ hình nền mặc định
            background_down=''  # Loại bỏ hình nền khi nhấn
        )

        # Tạo nút "Sign in" với màu nút #99CCFF
        signin_button = Button(
            text="Sign in",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            font_size='20sp',  # Phóng to chữ
            background_color=(0.6, 0.8, 1.0, 1.0),  # Màu #99CCFF
            background_normal='',  # Loại bỏ hình nền mặc định
            background_down=''  # Loại bỏ hình nền khi nhấn
        )

        # Thêm sự kiện khi nhấp vào nút "Log in"
        login_button.bind(on_press=self.go_to_login_screen)

        # Thêm sự kiện khi nhấp vào nút "Sign in"
        signin_button.bind(on_press=self.go_to_signin_screen)

        # Thêm các widget vào layout
        layout.add_widget(background)
        layout.add_widget(login_button)
        layout.add_widget(signin_button)

        # Thêm layout vào màn hình
        self.add_widget(layout)

    def go_to_login_screen(self, instance):
        # Chuyển sang màn hình đăng nhập
        self.manager.current = 'login'

    def go_to_signin_screen(self, instance):
        # Chuyển sang màn hình đăng ký
        self.manager.current = 'signin'

# Màn hình đăng nhập
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Tạo layout chính với FloatLayout
        layout = FloatLayout()

        # Thêm label để hiển thị thông báo
        label = Label(
            text="Welcome to Login Screen",
            font_size='24sp',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Thêm nút "Back" để quay lại màn hình chính
        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),  # Màu xám
            background_normal='',
            background_down=''
        )

        # Thêm sự kiện khi nhấp vào nút "Back"
        back_button.bind(on_press=self.go_back_to_main)

        # Thêm các widget vào layout
        layout.add_widget(label)
        layout.add_widget(back_button)

        # Thêm layout vào màn hình
        self.add_widget(layout)

    def go_back_to_main(self, instance):
        # Quay lại màn hình chính
        self.manager.current = 'main'

# Màn hình đăng ký
class SignInScreen(Screen):
    def __init__(self, **kwargs):
        super(SignInScreen, self).__init__(**kwargs)

        # Tạo layout chính với FloatLayout
        layout = FloatLayout()

        # Thêm label để hiển thị thông báo
        label = Label(
            text="Welcome to Sign In Screen",
            font_size='24sp',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Thêm nút "Back" để quay lại màn hình chính
        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),  # Màu xám
            background_normal='',
            background_down=''
        )

        # Thêm sự kiện khi nhấp vào nút "Back"
        back_button.bind(on_press=self.go_back_to_main)

        # Thêm các widget vào layout
        layout.add_widget(label)
        layout.add_widget(back_button)

        # Thêm layout vào màn hình
        self.add_widget(layout)

    def go_back_to_main(self, instance):
        # Quay lại màn hình chính
        self.manager.current = 'main'

# Lớp chính của ứng dụng
class MyApp(App):
    def build(self):
        # Tạo ScreenManager để quản lý các màn hình
        screen_manager = ScreenManager()

        # Thêm màn hình chính
        main_screen = MainScreen(name='main')
        screen_manager.add_widget(main_screen)

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