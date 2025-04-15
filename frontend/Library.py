from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup


class CommentItem(Label):
    def __init__(self, text, **kwargs):
        super(CommentItem, self).__init__(**kwargs)
        self.text = text
        self.size_hint_y = None
        self.height = 40
        self.halign = 'left'
        self.valign = 'middle'
        self.text_size = (self.width, None)
        self.color = (0, 0, 0, 1)  # Màu chữ đen
        self.bind(size=self._update_text_size)

    def _update_text_size(self, *args):
        self.text_size = (self.width, None)


class LibraryScreen(Screen):
    def __init__(self, **kwargs):
        super(LibraryScreen, self).__init__(**kwargs)

        layout = FloatLayout()
        self.bg = Image(source='background1.png', keep_ratio=False, allow_stretch=True)
        layout.add_widget(self.bg)

        # Scrollable content
        scroll_view = ScrollView(size_hint=(1, 0.8), pos_hint={"x": 0, "y": 0.25})  # Điều chỉnh vị trí để chừa chỗ cho thanh comment
        self.content = BoxLayout(orientation='vertical', size_hint_y=None, spacing=20, padding=20)
        self.content.bind(minimum_height=self.content.setter('height'))

        # Introduction text
        intro_text = (
            "The Vietnamese-German University (VGU) Library is not only an academic center but also a symbol of modern architecture and sustainable development in Vietnam.\n\n"
            "- Designed by Machado Silvetti.\n"
            "- Natural lighting & ventilation.\n"
            "- Green building model.\n"
            "- Databases: Springer, IEEE, JSTOR."
        )

        intro_label = Label(
            text=intro_text,
            size_hint_y=None,
            height=200,
            halign='justify',  # Căn đều hai bên
            valign='top',      # Căn dọc trên
            color=(0, 0, 0, 1),
            font_size='16sp'
        )

        # Cập nhật `text_size` dựa trên kích thước màn hình
        def update_text_size(instance, value):
            intro_label.text_size = (instance.width * 0.9, None)  # Chiều rộng bằng 90% màn hình

        self.bind(size=update_text_size)  # Gắn sự kiện thay đổi kích thước màn hình
        update_text_size(self, self.size[0])  # Gọi hàm để cập nhật ngay lập tức

        self.content.add_widget(intro_label)
        self.content.add_widget(Image(source='library1.png', size_hint_y=None, height=200))
        self.content.add_widget(Image(source='library2.png', size_hint_y=None, height=200))

        # Danh sách comment nằm trong nội dung cuộn
        self.comment_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.comment_list.bind(minimum_height=self.comment_list.setter('height'))
        self.content.add_widget(self.comment_list)

        scroll_view.add_widget(self.content)
        layout.add_widget(scroll_view)

        # Ô nhập comment (đặt ngoài ScrollView)
        comment_input_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.07), pos_hint={"x": 0, "y": 0}, spacing=5, padding=5)
        self.comment_input = TextInput(hint_text="Write a comment...", size_hint=(0.8, 1), multiline=False, background_color=(1, 1, 1, 1))
        submit_button = Button(text="Submit", size_hint=(0.2, 1), background_color=(0.2, 0.6, 0.2, 1))
        submit_button.bind(on_press=self.submit_comment)
        comment_input_box.add_widget(self.comment_input)
        comment_input_box.add_widget(submit_button)

        # Thêm thanh comment vào layout chính (ngoài ScrollView)
        layout.add_widget(comment_input_box)

        # Nút Share
        share_button = Button(
            text="📤 Share this article",
            size_hint=(0.5, 0.05),
            pos_hint={"right": 0.98, "top": 0.97},
            background_color=(0.2, 0.4, 0.8, 1)
        )
        share_button.bind(on_press=self.show_share_popup)
        layout.add_widget(share_button)

        self.add_widget(layout)

    def submit_comment(self, instance):
        comment = self.comment_input.text.strip()
        if comment:
            self.comment_list.add_widget(CommentItem(comment, size_hint_y=None, height=40))
            self.comment_input.text = ""

    def show_share_popup(self, instance):
        popup = Popup(
            title="Share",
            content=Label(text="✅ Shared with your friends (simulated)."),
            size_hint=(0.7, 0.3)
        )
        popup.open()


class LibraryApp(App):
    def build(self):
        return LibraryScreen()


if __name__ == "__main__":
    LibraryApp().run()