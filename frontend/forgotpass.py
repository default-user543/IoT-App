from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class ForgotPasswordScreen(Screen):
    def __init__(self, **kwargs):
        super(ForgotPasswordScreen, self).__init__(**kwargs)

        layout = FloatLayout()

        # Thêm hình nền 
        bg_image = Image(
            source='forgotpass.png',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )

        # Nút quay lại login
        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            font_size='20sp',
            background_color=(0.8, 0.8, 0.8, 1),
            background_normal='',
            background_down=''
        )
        back_button.bind(on_press=self.go_back_to_login)

        layout.add_widget(bg_image)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back_to_login(self, instance):
        self.manager.current = 'login_image'  # Đúng tên màn hình trong ScreenManager
