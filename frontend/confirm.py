from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ConfirmScreen(Screen):
    def __init__(self, **kwargs):
        super(ConfirmScreen, self).__init__(**kwargs)

        # Tạo layout chính
        layout = BoxLayout(orientation='vertical', spacing=20, padding=[20, 20, 20, 20])

        # Tiêu đề
        label = Label(text="Confirmation Screen", font_size='24sp')

        # Nút quay lại
        back_button = Button(text="Back", size_hint=(None, None), size=(100, 50))
        back_button.bind(on_press=self.go_back)

        # Thêm vào layout
        layout.add_widget(label)
        layout.add_widget(back_button)

        # Thêm layout vào màn hình
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'signin_image'
