from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.image import Image as CoreImage

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        
        def set_window_size(self):
            img = CoreImage('menu.png')
            width, height = img.size
            Window.size = (width*0.35, height*0.35)  
        set_window_size(self)

        layout = FloatLayout()
        self.bg = Image(source='menu.png', keep_ratio=False, allow_stretch=True)
        layout.add_widget(self.bg)
        
        # Tạo ScrollView
        scroll_view = ScrollView(
            size_hint=(0.4, 0.5), pos_hint =({'center_x': 0.5, 'center_y': 0.5})
            )
        
        # Tạo GridLayout bên trong ScrollView
        grid_layout = GridLayout(
            cols=1,
            size_hint_y=None,
            row_default_height=100,
            row_force_default=True,
            spacing=30,
            size_hint_x=1,
            width=300
        )
        grid_layout.bind(minimum_height=grid_layout.setter('height'))
        scroll_view.add_widget(grid_layout)

        # Thêm các nút vào GridLayout
        buttons = '[b]Lecture Hall[/b]', '[b]Dormitory[/b]', '[b]Library[/b]', '[b]Stadium[/b]', '[b]Canteen[/b]'
        for button_text in buttons:
            menubutton = Button(
                text = button_text,
                size_hint=(None, None),
                size=(200, 50),
                pos_hint={'center_x': 0.5},
                background_normal='',
                background_color=(0.2, 0.6, 1, 1),
                markup=True
            )
            menubutton.bind(on_press=self.go_to_relatedscreen)
            grid_layout.add_widget(menubutton)

        # Back button
        self.backbutton = Button(
            text='Back',
            size_hint=(None, None),
            size=(100, 50), 
            pos_hint={'left': 1, 'top': 1},
            background_normal='',
            background_color=(0.2, 0.6, 1, 1)
        )
        self.backbutton.bind(on_press=self.go_back_to_home)
        layout.add_widget(self.backbutton)

        self.add_widget(layout)

        self.add_widget(scroll_view)
    
    def go_back_to_home(self, instance):
        self.manager.current = 'home'

    def go_to_relatedscreen(self, instance):
        # Lấy tên nút được nhấn
        button_text = instance.text
        # Chuyển đổi tên nút thành tên screen tương ứng vd: 'Lecture Hall' -> 'hallscreen'
        screen_name = button_text.split(' ')[-1].lower() + 'screen'
        self.manager.current = screen_name

