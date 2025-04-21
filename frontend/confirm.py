from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle

# Thiết lập màu nền cho ứng dụng
Window.clearcolor = (1, 1, 1, 1)  # Màu trắng

class ConfirmScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Tạo layout chính với FloatLayout
        layout = FloatLayout()

        # Thêm hình nền
        background_image = Image(
            source='confirm.png',  # Đường dẫn đến hình nền
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        layout.add_widget(background_image)

        # Tạo dropdown cho câu hỏi bảo mật
        self.dropdown = DropDown()
        questions = ["The city where you live", "Your favourite colour", "Your favourite pet"]
        for question in questions:
            btn = Button(
                text=question,
                size_hint_y=None,
                height=44,
                background_color=(1, 1, 1, 1),  # Màu nền trắng
                color=(0.5, 0.5, 0.5, 1)       # Chữ màu xám
            )
            btn.bind(on_release=lambda btn: self.select_question(btn.text))
            self.dropdown.add_widget(btn)

        # Nút để hiển thị dropdown
        self.question_button = Button(
            text="Choose a security question",
            size_hint=(0.8, None),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            background_color=(0.95, 0.95, 0.95, 1),
            color=(0, 0, 0, 1)
        )
        self.question_button.bind(on_release=self.dropdown.open)
        layout.add_widget(self.question_button)

        # Khung nhập liệu cho câu trả lời
        self.answer_input = TextInput(
            hint_text="Your answer",
            size_hint=(0.8, None),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            background_color=(0.95, 0.95, 0.95, 1),
            foreground_color=(0, 0, 0, 1),
            hint_text_color=(0.5, 0.5, 0.5, 1)
        )
        layout.add_widget(self.answer_input)

        # Label hiển thị thông báo lỗi
        self.error_label = Label(
            text="",
            size_hint=(1, None),
            height=30,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            color=(1, 0, 0, 1)  # Màu đỏ cho lỗi
        )
        layout.add_widget(self.error_label)

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

        # Nút Submit
        submit_button = RoundedButton(
            text="Submit",
            size_hint=(None, None),
            size=(120, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),
            color=(1, 1, 1, 1)
        )
        submit_button.bind(on_press=self.submit)
        layout.add_widget(submit_button)

        # Nút Back để quay về SignIn
        back_button = RoundedButton(
            text="Back",
            size_hint=(None, None),
            size=(120, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),
            color=(1, 1, 1, 1)
        )
        back_button.bind(on_press=self.go_back_to_signin)
        layout.add_widget(back_button)

        # Thêm layout vào màn hình
        self.add_widget(layout)

    def select_question(self, question):
        self.question_button.text = question
        self.dropdown.dismiss()
        self.error_label.text = ""  # Xóa thông báo lỗi nếu có

    def submit(self, instance):
        selected_question = self.question_button.text
        answer = self.answer_input.text.strip()

        # Kiểm tra nếu người dùng chưa chọn câu hỏi
        if selected_question == "Choose a security question":
            self.error_label.text = "Error! Please choose one security question"
            return

        # Kiểm tra nếu người dùng chưa nhập câu trả lời
        if not answer:
            self.error_label.text = "Error! Please fill in this box"
            return

        # Nếu hợp lệ, chuyển sang màn hình đăng nhập
        self.manager.current = 'login_image'

    def go_back_to_signin(self, instance):
        self.manager.current = 'signin_image'