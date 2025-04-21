from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle

class SignInImageScreen(Screen):
    def __init__(self, **kwargs):
        super(SignInImageScreen, self).__init__(**kwargs)

        # Tạo layout chính với FloatLayout
        layout = FloatLayout()

        # Thêm hình nền
        signin_image = Image(
            source='signin.png',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )

        # Tạo BoxLayout để chứa các khung nhập liệu
        input_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            spacing=20,
            padding=[20, 20, 20, 20]
        )

        # Tạo khung nhập liệu cho "User's name"
        self.username_input = self.create_rounded_input("User's name")
        # Tạo khung nhập liệu cho "Password"
        self.password_input = self.create_rounded_input("Password", password=True)
        # Tạo khung nhập liệu cho "Confirm Password"
        self.confirm_password_input = self.create_rounded_input("Confirm Password", password=True)

        # Thêm các khung nhập liệu vào BoxLayout
        input_layout.add_widget(self.username_input)
        input_layout.add_widget(self.password_input)
        input_layout.add_widget(self.confirm_password_input)

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

        # Thêm nút "Next"
        next_button = RoundedButton(
            text="Next",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),
            background_normal='',
            background_down=''
        )
        next_button.bind(on_press=self.validate_inputs)

        # Thêm nút "Already have an account?"
        login_button = Button(
            text="Already have an account?",
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            font_size='18sp',
            background_color=(0, 0, 0, 0),
            color=(1, 1, 1, 1),
            background_normal='',
            background_down=''
        )
        login_button.bind(on_press=self.go_to_login)

        # Thêm các widget vào layout
        layout.add_widget(signin_image)
        layout.add_widget(input_layout)
        layout.add_widget(next_button)
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

    def validate_inputs(self, instance):
        """Kiểm tra đầu vào và hiển thị lỗi nếu cần."""
        username = self.username_input.children[0].text.strip()
        password = self.password_input.children[0].text.strip()
        confirm_password = self.confirm_password_input.children[0].text.strip()

        # Kiểm tra nếu các trường bị bỏ trống
        if not username:
            self.username_input.children[0].hint_text = "Please fill in this box"
            self.username_input.children[0].hint_text_color = (1, 0, 0, 1)
            return
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

        # Nếu hợp lệ, chuyển sang màn hình confirm
        self.manager.current = 'confirm'

    def go_to_login(self, instance):
        """Chuyển sang màn hình login."""
        self.manager.current = 'login_image'