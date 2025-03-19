from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle

class LoginImageScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginImageScreen, self).__init__(**kwargs)

        # Tạo layout chính với FloatLayout
        layout = FloatLayout()

        # Thêm hình ảnh đăng nhập (signin.png)
        login_image = Image(
            source='login.png',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )

        # Tạo BoxLayout để chứa các khung nhập liệu
        input_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.3),  # Giảm chiều cao
            pos_hint={'center_x': 0.5, 'center_y': 0.35},  
            spacing=10,
            padding=[20, 20, 20, 20]
        )

        # Tạo khung nhập liệu cho "Users name"
        username_input = self.create_rounded_input("Username")
        # Tạo khung nhập liệu cho "Password"
        password_input = self.create_rounded_input("Password", password=True)
        
        # Nút "Forgot Password?"
        forgot_password_button = self.create_rounded_button("Forgot Password?", self.on_forgot_password)

        # Thêm các khung nhập vào BoxLayout
        input_layout.add_widget(username_input)
        input_layout.add_widget(password_input)
        input_layout.add_widget(forgot_password_button)

        # Nút "Back"
        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},  # Giữ nguyên vị trí
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),
            background_normal='',
            background_down=''
        )
        back_button.bind(on_press=self.go_back_to_main)

        # Thêm các widget vào layout
        layout.add_widget(login_image)
        layout.add_widget(input_layout)
        layout.add_widget(back_button)

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

    def create_rounded_button(self, text, on_press_callback):
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
        button = Button(
            text=text,
            size_hint=(1, None),
            height=40,
            font_size='18sp',
            background_color=(0, 0, 0, 0),
            color=(0.3, 0.3, 0.3, 1),
            background_normal='',
            background_down=''
        )
        button.bind(on_press=on_press_callback)
        box.add_widget(button)
        box.bind(pos=self.update_rect, size=self.update_rect)
        return box

    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def go_back_to_main(self, instance):
        self.manager.current = 'main'

    def on_forgot_password(self, instance):
        self.manager.current = 'forgotpass'  #  Chuyển sang màn hình Forgot Password