from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle

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

        # Tạo khung nhập liệu cho "Username"
        username_input = self.create_rounded_input("Username")
        # Tạo khung nhập liệu cho "Password"
        password_input = self.create_rounded_input("Password", password=True)
        # Tạo khung nhập liệu cho "Confirm password"
        confirm_password_input = self.create_rounded_input("Confirm password", password=True)

        # Thêm các khung nhập liệu vào BoxLayout
        input_layout.add_widget(username_input)
        input_layout.add_widget(password_input)
        input_layout.add_widget(confirm_password_input)

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
        back_button.bind(on_press=self.go_back_to_main)

        # Thêm nút "Next" phía trên nút "Back"
        next_button = Button(
            text="Next",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),
            background_normal='',
            background_down=''
        )
        next_button.bind(on_press=self.go_to_confirm)

        # Thêm các widget vào layout
        layout.add_widget(signin_image)
        layout.add_widget(input_layout)
        layout.add_widget(next_button)
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

    def go_to_confirm(self, instance):
        # Chuyển sang màn hình confirm
        self.manager.current = 'confirm'