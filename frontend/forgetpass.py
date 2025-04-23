from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
import requests
import json

# Set background color for the app
Window.clearcolor = (1, 1, 1, 1)  # White background

# Forget Password Screen with Image
class ForgetpwImageScreen(Screen):
    def __init__(self, **kwargs):
        super(ForgetpwImageScreen, self).__init__(**kwargs)

        # Create main layout
        self.layout = FloatLayout()

        # Add background image
        login_image = Image(
            source='forgotpass.png',  # Ensure the path to the image is correct
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )

        # Create input fields layout
        self.input_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.4),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            spacing=10,
            padding=[20, 20, 20, 20]
        )

        # Add dropdown for "Question"
        self.dropdown = DropDown()
        questions = ["Your favourite pet", "Your favourite colour", "The city where you live"]
        for question in questions:
            btn = Button(
                text=question,
                size_hint_y=None,
                height=44,
                background_normal='',  # Loại bỏ hình nền mặc định
                background_color=(1, 1, 1, 1),  # Nền trắng
                color=(0, 0, 0, 1)  # Chữ đen
            )
            btn.bind(on_release=lambda btn: self.select_question(btn.text))
            self.dropdown.add_widget(btn)

        # Button to display dropdown
        self.question_button = Button(
            text="Choose a security question",
            size_hint=(1, None),
            height=50,
            background_normal='',  # Loại bỏ hình nền mặc định
            background_color=(1, 1, 1, 1),  # Nền trắng
            color=(0, 0, 0, 1)  # Chữ đen
        )
        self.question_button.bind(on_release=self.dropdown.open)
        self.input_layout.add_widget(self.question_button)

        # Add input field for "Answer"
        self.answer_input = self.create_rounded_input("Answer")
        self.input_layout.add_widget(self.answer_input)

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

        # Add "Submit" button
        submit_button = RoundedButton(
            text="Submit",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.32},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),
            background_normal='',
            background_down=''
        )
        submit_button.bind(on_press=self.validate_inputs)

        # Add "Back" button
        back_button = RoundedButton(
            text="Back",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1.0),
            background_normal='',
            background_down=''
        )
        back_button.bind(on_press=self.go_back_to_login)

        # Add widgets to layout
        self.layout.add_widget(login_image)
        self.layout.add_widget(self.input_layout)
        self.layout.add_widget(submit_button)
        self.layout.add_widget(back_button)

        # Add layout to screen
        self.add_widget(self.layout)

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

        # Bind event to clear error when user starts typing
        text_input.bind(on_text=self.clear_error)

        box.add_widget(text_input)
        box.bind(pos=self.update_rect, size=self.update_rect)
        return box

    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def select_question(self, question):
        self.question_button.text = question
        self.dropdown.dismiss()

    def validate_inputs(self, instance):
        # Check if inputs are empty and show error if needed
        selected_question = self.question_button.text
        answer = self.answer_input.children[0]

        has_error = False

        if selected_question == "Choose a security question":
            self.question_button.text = "Please choose a security question"
            self.question_button.color = (1, 0, 0, 1)  # Red color
            has_error = True
        if not answer.text.strip():
            answer.hint_text = "Error! Please fill in the box"
            answer.hint_text_color = (1, 0, 0, 1)  # Red color
            has_error = True

        # If no errors, navigate to the change password screen
        if not has_error:
            self.go_to_changepassword(instance)

    def clear_error(self, instance, value):
        # Clear error when user starts typing
        if instance.hint_text == "Error! Please fill in the box":
            instance.hint_text = instance.hint_text.replace("Error! Please fill in the box", "")
            instance.hint_text_color = (0.5, 0.5, 0.5, 1)  # Reset to grey color

    def go_back_to_login(self, instance):
        # Navigate back to the login screen
        self.manager.current = 'login_image'

    def go_to_changepassword(self, instance):

        if self.question_button.text == "Your favourite pet":
            pet_answer = self.answer_input.children[0].text.strip()
            colour_answer = ""
            city_answer = ""
        elif self.question_button.text == "Your favourite colour":
            colour_answer = self.answer_input.children[0].text.strip()
            pet_answer = ""
            city_answer = ""
        elif self.question_button.text == "The city where you live":
            city_answer = self.answer_input.children[0].text.strip()
            pet_answer = ""
            colour_answer = ""

        # Gửi request tới backend
        url = "http://127.0.0.1:5000/forgot-password"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "city": city_answer,
            "fav_colour": colour_answer,
            "fav_pet": pet_answer,
        }

        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.status_code == 200:
                print("Successful!")
                self.manager.current = 'change_password_image' # Nếu hợp lệ, chuyển sang màn hình confirm
            else:
                data = response.json()
                print("Error:", data.get("message"))
        except requests.exceptions.RequestException as e:
            print("Failed to connect to backend:", e)
