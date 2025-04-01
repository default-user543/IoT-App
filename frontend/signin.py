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

import requests
import json
BACKEND_URL = ""

# Màn hình hình ảnh đăng ký
class SignInImageScreen(Screen):
    def __init__(self, **kwargs):
        super(SignInImageScreen, self).__init__(**kwargs)

        # Tạo layout chính với FloatLayout
        layout = FloatLayout()

        # Thêm hình ảnh đăng ký
        signin_image = Image(
            source='signin.png',
            allow_stretch=True,  # Cho phép kéo dãn hình ảnh
            keep_ratio=False,    # Không giữ tỷ lệ khung hình
            size_hint=(1, 1),    # Lấp đầy toàn bộ màn hình
            pos_hint={'x': 0, 'y': 0}  # Bắt đầu từ góc dưới bên trái
        )

        # Tạo BoxLayout để chứa các khung nhập liệu
        input_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            spacing=20,
            padding=[20, 20, 20, 20]
        )

        # Tạo khung nhập liệu cho "User name"
        username_input = self.create_rounded_input("User name")
        # Tạo khung nhập liệu cho "Password"
        password_input = self.create_rounded_input("Password", password=True)
        # Tạo khung nhập liệu cho "Confirm password"
        confirm_password_input = self.create_rounded_input("Confirm password", password=True)

        # Thêm các khung nhập liệu vào BoxLayout
        input_layout.add_widget(username_input)
        input_layout.add_widget(password_input)
        input_layout.add_widget(confirm_password_input)

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

        # Thêm nút "Back" để quay lại màn hình chính
        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),  # Màu xám
            background_normal='',
            background_down=''
        )

        # Label hiển thị thông báo
        self.message_label = Label(
            text="",
            color=(1, 0, 0, 1),  # Màu đỏ cho thông báo lỗi
            font_size='18sp',
            pos_hint={'center_x': 0.5, 'center_y': 0.25}
        )

        # Thêm sự kiện khi nhấp vào nút "Back"
        back_button.bind(on_press=self.go_back_to_main)

        # Thêm các widget vào layout
        layout.add_widget(signin_image)
        layout.add_widget(input_layout)
        layout.add_widget(submit_button)
        layout.add_widget(back_button)

        # Thêm layout vào màn hình
        self.add_widget(layout)

    def create_rounded_input(self, hint_text, password=False):
        # Tạo một BoxLayout để chứa TextInput và bo góc
        box = BoxLayout(
            orientation='vertical',
            size_hint=(1, None),
            height=50,
            padding=[10, 10, 10, 10]
        )

        # Sử dụng canvas để vẽ hình chữ nhật bo góc
        with box.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # Màu nền của khung
            box.rect = RoundedRectangle(
                pos=box.pos,
                size=box.size,
                radius=[10,]
            )

        # Tạo TextInput
        text_input = TextInput(
            hint_text=hint_text,
            size_hint=(1, None),
            height=40,
            background_color=(0, 0, 0, 0),  # Trong suốt
            foreground_color=(0, 0, 0, 1),  # Màu chữ đen
            hint_text_color=(0.5, 0.5, 0.5, 1),  # Màu chữ gợi ý
            password=password  # Ẩn văn bản nếu là mật khẩu
        )

        # Thêm TextInput vào BoxLayout
        box.add_widget(text_input)

        # Cập nhật hình chữ nhật khi kích thước thay đổi
        box.bind(pos=self.update_rect, size=self.update_rect)

        return box

    def update_rect(self, instance, value):
        # Cập nhật vị trí và kích thước của hình chữ nhật bo góc
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def go_back_to_main(self, instance):
        # Quay lại màn hình chính
        self.manager.current = 'main'

    def sign_up(self, instance):
        """ Gửi dữ liệu đăng ký lên backend """
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        confirm_password = self.confirm_password_input.text.strip()

        if not username or not password or not confirm_password:
            self.message_label.text = "Please fill in all fields!"
            return

        if password != confirm_password:
            self.message_label.text = "Passwords do not match!"
            return

        # Gửi request đến backend
        data = {
            "username": username,
            "password": password,
            "confirm_password": confirm_password
        }

        try:
            response = requests.post(BACKEND_URL, json=data)
            result = response.json()
            
            if response.status_code == 200:
                self.message_label.color = (0, 1, 0, 1)  # Màu xanh cho thành công
                self.message_label.text = "Sign up successful!"
            else:
                self.message_label.text = result.get("message", "Sign up failed!")

        except requests.exceptions.RequestException as e:
            self.message_label.text = "Error connecting to server!"
            print(f"Error: {e}")


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

        # Nút Submit
        submit_button = Button(
            text="Submit",
            size_hint=(None, None),
            size=(120, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},  # Điều chỉnh vị trí
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),
            color=(1, 1, 1, 1)
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