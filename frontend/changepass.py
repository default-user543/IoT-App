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
import requests
import json

# Thiết lập màu nền cho ứng dụng
Window.clearcolor = (1, 1, 1, 1)  # Màu trắng

# Màn hình hình ảnh đăng nhập
class ChangepwImageScreen(Screen):
    def __init__(self, **kwargs):
        super(ChangepwImageScreen, self).__init__(**kwargs)
        # Tạo layout chính với FloatLayout
        layout = FloatLayout()

        # Thêm hình ảnh cho trang cp bằng ảnh đăng nhập
        login_image = Image(
            source='login.png',
            allow_stretch=True,  # Cho phép kéo dãn hình ảnh
            keep_ratio=False,    # Không giữ tỷ lệ khung hình
            size_hint=(1, 1),    # Lấp đầy toàn bộ màn hình
            pos_hint={'x': 0, 'y': 0}  # Bắt đầu từ góc dưới bên trái
        )

        # Tạo BoxLayout để chứa các khung nhập liệu
        self.input_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.4),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            spacing=20,
            padding=[20, 20, 20, 20]
        )

        # Tạo khung nhập liệu cho "User's name"
        self.password_input = self.create_rounded_input("New Password", password = True)
        # Tạo khung nhập liệu cho "Keyword"
        self.confirm_password_input = self.create_rounded_input("Confirm Password", password = True)

        # Thêm các khung nhập liệu vào BoxLayout
        self.input_layout.add_widget(self.password_input)
        self.input_layout.add_widget(self.confirm_password_input)

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

        # Thêm nút "Back" để quay lại trang login
        submit_button = RoundedButton(
            text="Submit",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),  # Màu xám
            background_normal='',
            background_down=''
        )

        # Thêm sự kiện khi nhấp vào nút "Back"
        submit_button.bind(on_press=self.go_back_to_main)

        # Thêm các widget vào layout
        layout.add_widget(login_image)
        layout.add_widget(self.input_layout)
        layout.add_widget(submit_button)

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
        # Quay lại màn hình main
        self.manager.current = 'main'



# Màn hình đăng nhập
class ChangepwScreen(Screen):
    def __init__(self, **kwargs):
        super(ChangepwScreen, self).__init__(**kwargs)

        # Tạo layout chính với FloatLayout
        layout = FloatLayout()

        # Thêm label để hiển thị thông báo
        label = Label(
            text="Forget Password?",
            font_size='24sp',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        # Thêm nút "Back" để quay lại màn hình chính
        submit_button = Button(
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
        submit_button.bind(on_press=self.go_back_to_main)

        # Thêm các widget vào layout
        layout.add_widget(label)
        layout.add_widget(submit_button)

        # Thêm layout vào màn hình
        self.add_widget(layout)

    def go_back_to_main(self, instance):
        """Kiểm tra đầu vào và hiển thị lỗi nếu cần."""
        username = self.username_input.children[0].text.strip()
        password = self.password_input.children[0].text.strip()
        confirm_password = self.confirm_password_input.children[0].text.strip()

        # Kiểm tra nếu các trường bị bỏ trống        
        if not password:
            self.password_input.children[0].hint_text = "Please fill in this box"
            self.password_input.children[0].hint_text_color = (1, 0, 0, 1)
            return
        if not confirm_password:
            self.confirm_password_input.children[0].hint_text = "Please fill in this box"
            self.confirm_password_input.children[0].hint_text_color = (1, 0, 0, 1)
            return
    

        # Kiểm tra nếu mật khẩu không khớp
        if password != confirm_password:
            self.confirm_password_input.children[0].hint_text = "Confirm wrong"
            self.confirm_password_input.children[0].hint_text_color = (1, 0, 0, 1)
            return
        
        # Gửi request tới backend
        url = "http://127.0.0.1:5000/forgot-password"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "new_password": password
        }

        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.status_code == 200:
                print("Sign-up successful!")
                self.manager.current = 'main' # Nếu hợp lệ, chuyển sang màn hình confirm
            else:
                data = response.json()
                print("Error:", data.get("message"))
        except requests.exceptions.RequestException as e:
            print("Failed to connect to backend:", e)

