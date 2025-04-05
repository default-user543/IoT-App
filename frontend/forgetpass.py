from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

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
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            spacing=10,
            padding=[20, 20, 20, 20]
        )

        # Add input fields
        self.username_input = self.create_rounded_input("User's name")
        self.question_input = self.create_rounded_input("Question")
        self.answer_input = self.create_rounded_input("Answer")

        # Add input fields to layout
        self.input_layout.add_widget(self.username_input)
        self.input_layout.add_widget(self.question_input)
        self.input_layout.add_widget(self.answer_input)

        # Add "Submit" button
        submit_button = Button(
            text="Submit",
            size_hint=(None, None),
            size=(100, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.13},
            font_size='15sp',
            background_color=(0.8, 0.8, 0.8, 1.0),
            background_normal='',
            background_down=''
        )
        submit_button.bind(on_press=self.validate_inputs)

        # Add "Back" button
        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.04},
            font_size='15sp',
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

    def validate_inputs(self, instance):
        # Check if inputs are empty and show error if needed
        username = self.username_input.children[0]
        question = self.question_input.children[0]
        answer = self.answer_input.children[0]

        has_error = False

        if not username.text.strip():
            username.hint_text = "Error! Please fill in the box"
            username.hint_text_color = (1, 0, 0, 1)  # Red color
            has_error = True
        if not question.text.strip():
            question.hint_text = "Error! Please fill in the box"
            question.hint_text_color = (1, 0, 0, 1)  # Red color
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
        # Navigate to the change password screen
        self.manager.current = 'change_password'