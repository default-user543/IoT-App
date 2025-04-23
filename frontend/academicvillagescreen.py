from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.core.image import Image as CoreImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stencilview import StencilView
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.relativelayout import RelativeLayout
import requests
import json


class AcademicVillageScreen(Screen):
    def __init__(self, **kwargs):
        super(AcademicVillageScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        self.set_window_size()
        self.bg = Image(source='academicvillage.png', keep_ratio=False, allow_stretch=True)
        layout.add_widget(self.bg)

        class RoundedScrollView(StencilView):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                with self.canvas.before:
                    Color(1, 1, 1, 1)  # White background
                    self.bg = RoundedRectangle(radius=[20], pos=self.pos, size=self.size)

                self.bind(pos=self.update_bg, size=self.update_bg)

            def update_bg(self, *args):
                self.bg.pos = self.pos
                self.bg.size = self.size

        # Tạo header
        self.header = BoxLayout(
            size_hint_y=None,
            height='40dp',
            padding=(10, 0, 10, 0),
            spacing=20,
            pos_hint={'top': 1}
        )
        with self.header.canvas.before:
            Color(0.694, 0.875, 0.980, 1)  # background màu xám đậm
            rect = Rectangle(pos=self.header.pos, size=self.header.size)

        self.header.bind(pos=lambda *args: setattr(rect, 'pos', self.header.pos))
        self.header.bind(size=lambda *args: setattr(rect, 'size', self.header.size))

        # Back
        back = RelativeLayout(size_hint_x=None, width='30dp', height='30dp')

        back_button = Button(background_normal='', background_down='', background_color=(0, 0, 0, 0))
        back_button.bind(on_press=self.back_to_menu)

        img = Image(
            source='back_icon.png',
            allow_stretch=True,
            size_hint=(1, 1)
        )
        back.add_widget(img)
        back.add_widget(back_button)
        self.header.add_widget(back)

        # Username box
        username_box = BoxLayout(
            size_hint=(None, None),
            size_hint_x=0.7,
            height='35dp',  # tùy chỉnh
            padding=(20, 0),
            pos_hint={'center_y': 0.5}
        )

        with username_box.canvas.before:
            Color(0.204, 0.553, 0.761, 1)  # Màu nền xanh dương nhạt
            rounded_rect = RoundedRectangle(
                size=username_box.size,
                pos=username_box.pos,
                radius=[20]  # bo tròn 4 góc
            )

        # cập nhật lại khi size/pos thay đổi
        def update_rect(*args):
            rounded_rect.pos = username_box.pos
            rounded_rect.size = username_box.size

        username_box.bind(pos=update_rect, size=update_rect)

        # Username
        name = Label(
            text='Welcome to Academic Village!',
            color=(0.694, 0.875, 0.980, 1),
            halign='left',
            valign='middle'
        )
        name.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        username_box.add_widget(name)
        self.header.add_widget(username_box)

       

        # Log out
        logout = RelativeLayout(size_hint_x=None, width='30dp', height='30dp')

        logout_button = Button(background_normal='', background_down='', background_color=(0, 0, 0, 0))
        logout_button.bind(on_press=self.go_back_to_home)

        img = Image(
            source='signout_logo.png',
            allow_stretch=True,
            size_hint=(1, 1)
        )
        logout.add_widget(img)
        logout.add_widget(logout_button)
        self.header.add_widget(logout)

        # Hiển thị header
        layout.add_widget(self.header)

        # Scrollable area
        self.scroll_view = ScrollView(
            size_hint=(1, None),
            size=(Window.width, Window.height - 35),
            pos=(0, 0)
        )
        self.grid_layout = GridLayout(
            cols=1,
            size_hint_y=None,
            spacing=25,
            padding=(10, 35, 10, 20)
        )
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))

        texts = "Academic Village to welcome visiting lecturers and professors from other countries, serving the goal of building strategic cooperation with international educational institutions."

        scroll_box_height = 0.8 * Window.size[1]

        class StyledButton(ButtonBehavior, BoxLayout):
            def __init__(self, text, **kwargs):
                super().__init__(**kwargs)
                self.padding = 0
                self.size_hint_y = None
                self.height = scroll_box_height
                with self.canvas.before:
                    Color(0.694, 0.875, 0.980, 0.5)
                    self.rect = RoundedRectangle(radius=[15])
                self.bind(pos=self.update_rect, size=self.update_rect)

                self.label = Label(text=texts, color=(1, 1, 1, 1), font_size='16sp', bold=True, halign='left', valign='middle', padding=(15, 0))
                self.label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
                self.add_widget(self.label)

            def update_rect(self, *args):
                self.rect.pos = self.pos
                self.rect.size = self.size

        # Thanh cuộn ngang chứa hình ảnh
        image_scroll_view = ScrollView(
            size_hint=(1, None),
            height=150,  # Chiều cao của thanh cuộn ngang
            do_scroll_x=True,
            do_scroll_y=False
        )

        image_container = BoxLayout(
            orientation='horizontal',
            size_hint_x=None,
            height=150,  # Chiều cao của các hình ảnh
            spacing=10,  # Khoảng cách giữa các hình ảnh
            padding=(10, 0)
        )
        image_container.bind(minimum_width=image_container.setter('width'))  # Đảm bảo kích thước thay đổi theo số lượng ảnh

        # Thêm các hình ảnh vào container
        image_sources = ['academicvillage1.png', 'academicvillage2.png', 'academicvillage3.png', 'academicvillage4.png', 'academicvillage5.png']  # Thay bằng đường dẫn ảnh của bạn
        for source in image_sources:
            img = Image(
                source=source,
                size_hint=(None, None),
                size=(200, 150),  # Kích thước mỗi hình ảnh
                allow_stretch=True,
                keep_ratio=True
            )
            image_container.add_widget(img)

        # Thêm container vào ScrollView
        image_scroll_view.add_widget(image_container)

        # Thêm thanh cuộn ngang vào layout chính trước phần text
        self.grid_layout.add_widget(image_scroll_view)

        # Thêm nút chứa text
        btn = StyledButton(text=texts)
        self.grid_layout.add_widget(btn)

        self.scroll_view.add_widget(self.grid_layout)
        layout.add_widget(self.scroll_view)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_back_to_home(self, instance):

        # Gửi request tới backend
        url = "http://127.0.0.1:5000/logout"
        headers = {'Content-Type': 'application/json'}
        

        try:
            payload = {}  # Define payload as an empty dictionary or add necessary data
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.status_code == 200:
                print("Log out successful!")
                self.manager.current = 'login_image' 
        except requests.exceptions.RequestException as e:
            print("Failed to connect to backend:", e)


    def share_button_pressed(self, instance):
        pass  # Add functionality here if needed

    def set_window_size(self):
        img = CoreImage('academicvillage.png')
        width, height = img.size
        Window.size = (width * 0.35, height * 0.35)

    def back_to_menu(self, instance):
        self.manager.current = 'menu'
        self.manager.transition.direction = 'right'