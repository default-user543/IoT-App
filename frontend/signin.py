from kivy.app import App
from kivy.uix.screenmanager import Screen
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

class SignInImageScreen(Screen):
    def __init__(self, **kwargs):
        super(SignInImageScreen, self).__init__(**kwargs)

        # Tạo layout chính với FloatLayout
        layout = FloatLayout()

        # Thêm hình ảnh đăng ký
        signin_image = Image(
            source='signin.png',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )

        # Tạo BoxLayout để chứa các khung nhập liệu
        self.input_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            spacing=20,
            padding=[20, 20, 20, 20]
        )

        # Tạo khung nhập liệu
        self.username_input = self.create_rounded_input("User name")
        self.password_input = self.create_rounded_input("Password", password=True)
        self.confirm_password_input = self.create_rounded_input("Confirm password", password=True)

        # Thêm các khung nhập liệu vào layout
        self.input_layout.add_widget(self.username_input)
        self.input_layout.add_widget(self.password_input)
        self.input_layout.add_widget(self.confirm_password_input)

        # Thêm Label để hiển thị thông báo lỗi
        self.message_label = Label(
            text="",
            size_hint=(1, None),
            height=30,
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            color=(1, 0, 0, 1)  # Màu đỏ cho lỗi
        )
        layout.add_widget(self.message_label)

        # Nút Submit
        submit_button = Button(
            text="Submit",
            size_hint=(None, None),
            size=(120, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.18},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),
            color=(1, 1, 1, 1)
        )
        submit_button.bind(on_press=self.sign_up)

        # Nút "already have an account?"
        login_button = Button(
            text="already have an account?",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            font_size='15sp',
            background_color=(0, 0, 0, 0),
            color=(0.5, 0.5, 0.5, 1)
        )
        login_button.bind(on_press=self.go_back_to_login_image)

        # Thêm các widget vào layout
        layout.add_widget(signin_image)
        layout.add_widget(self.input_layout)
        layout.add_widget(submit_button)
        layout.add_widget(login_button)

        # Thêm layout vào màn hình
        self.add_widget(layout)

    def create_rounded_input(self, hint_text, password=False):
        box = BoxLayout(
            orientation='vertical',
            size_hint=(1, None),
            height=50,
            padding=[10, 10, 10, 10]
        )
        with box.canvas.before:
            Color(0.95, 0.95, 0.95, 1)
            box.rect = RoundedRectangle(
                pos=box.pos,
                size=box.size,
                radius=[10,]
            )
        text_input = TextInput(
            hint_text=hint_text,
            size_hint=(1, None),
            height=40,
            background_color=(0, 0, 0, 0),
            foreground_color=(0, 0, 0, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1),
            password=password
        )
        box.add_widget(text_input)
        box.bind(pos=self.update_rect, size=self.update_rect)
        return box

    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def go_back_to_login_image(self, instance):
        self.manager.current = 'login_image'

    def sign_up(self, instance):
        username = self.username_input.children[0].text.strip()
        password = self.password_input.children[0].text.strip()
        confirm_password = self.confirm_password_input.children[0].text.strip()

        # Reset error message
        self.message_label.text = ""

        if not username or not password or not confirm_password:
            self.message_label.text = "Please fill in all fields!"
            return

        if password != confirm_password:
            self.message_label.text = "Passwords do not match!"
            return

        # Nếu tất cả thông tin hợp lệ
        self.message_label.color = (0, 1, 0, 1)  # Màu xanh cho thành công
        self.message_label.text = "Sign up successful!"