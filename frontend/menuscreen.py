from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.core.image import Image as CoreImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy_garden.mapview import MapView, MapMarkerPopup

Window.clearcolor = (1, 1, 1, 1) 

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical', spacing=10)

        # Header
        header = BoxLayout(size_hint_y=None, height='50dp', padding=(10, 0, 10, 10), spacing = 20)
        with header.canvas.before:
            Color(0.694, 0.878, 0.980, 1)  # background màu xám đậm
            rect = Rectangle(pos=header.pos, size=header.size)

        header.bind(pos=lambda *args: setattr(rect, 'pos', header.pos))
        header.bind(size=lambda *args: setattr(rect, 'size', header.size))

        # Username box
        username_box = BoxLayout(
            size_hint=(0.7, None),
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
            text='Username',
            color=(0.694, 0.875, 0.980, 1),
            halign='left', 
            valign='middle'
        )
        name.bind(size=lambda instance, value: setattr(instance, 'text_size', value))


        username_box.add_widget(name)
        header.add_widget(username_box)

        # Share
        share = RelativeLayout(size_hint_x=None, width='30dp', height='30dp')

        share_button = Button(background_normal='', background_down='', background_color=(0, 0, 0, 0))
        
        img = Image(
            source = 'share_logo.png', 
            allow_stretch=True, 
            size_hint = (1, 1)
            )
        share.add_widget(img)
        share.add_widget(share_button)
        header.add_widget(share)



        # Log out
        logout = RelativeLayout(size_hint_x=None, width='30dp', height='30dp')

        logout_button = Button(background_normal='', background_down='', background_color=(0, 0, 0, 0))
        logout_button.bind(on_press=self.go_back_to_home)

        img = Image(
            source = 'signout_logo.png', 
            allow_stretch=True, 
            size_hint = (1, 1)
            )
        logout.add_widget(img)
        logout.add_widget(logout_button)
        header.add_widget(logout)

        main_layout.add_widget(header)

        # Thêm widget bản đồ ở đây
        map_container = BoxLayout(padding=(10, 10), size_hint_y=None, height='410dp')  # có padding
        main_layout.add_widget(map_container)

        

        mapview = MapView(zoom=17, lat=10.762622, lon=106.660172)  # Ví dụ: Tọa độ HCM
        marker = MapMarkerPopup(lat=10.762622, lon=106.660172)
        mapview.add_widget(marker)

        map_container.add_widget(mapview)

        
        # Scrollable area
        scroll_view = ScrollView(size_hint_y = 1)
        grid_layout = GridLayout(cols=1, size_hint_y=None, spacing=25, padding=(10, 20))
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        # Các khối xanh biển
        items = [
            ("Lecture Hall", "1 m"),
            ("Sport Hall", "5 m"),
            ("Canteen", "30 m"),
            ("Library", "35 m"),
            ("Dormitory", "50 m"),
            ("Cluster Hall", "60 m"),
            ("Ceremony Hall", "70 m"),
            ("Administration Building", "80 m"),
            ("Academic Village", "90 m")
            
        ]

        items.sort(key=lambda x: int(x[1].split()[0]))

        class StyledButton(ButtonBehavior, BoxLayout):
            def __init__(self, text1, text2, **kwargs):
                super().__init__(**kwargs)
                self.padding = 10
                self.size_hint_y = None
                self.height = '100dp'
                with self.canvas.before:
                    Color(0.204, 0.553, 0.761, 1)
                    self.rect = RoundedRectangle(radius=[15])
                self.bind(pos=self.update_rect, size=self.update_rect)

                self.label1 = Label(text= text1, color=(1, 1, 1, 1), font_size='16sp', bold=True, halign='left', valign='middle', padding=(15, 0))
                self.label1.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
                self.label2 = Label(text= text2, color=(1, 1, 1, 1), font_size='16sp', bold=True, halign='right', valign='middle', padding=(15, 0))
                self.label2.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
                self.add_widget(self.label1)
                self.add_widget(self.label2)

            def update_rect(self, *args):
                self.rect.pos = self.pos
                self.rect.size = self.size

        for item, distance in items:
            btn = StyledButton(text1=item, text2=distance)
            btn.place_name = item  # Gắn tên địa điểm vào button
            btn.bind(on_press=self.go_to_relatedscreen)
            grid_layout.add_widget(btn)

        scroll_view.add_widget(grid_layout)
        main_layout.add_widget(scroll_view)

        

        self.add_widget(main_layout)

    
    def go_back_to_home(self, instance):
        self.manager.current = 'home'

    def go_to_relatedscreen(self, instance):
        # Lấy tên nút được nhấn
        place_name = instance.place_name
        screen_name = place_name.replace(' ', '').lower() + 'screen'
        self.manager.current = screen_name

