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
from kivy.graphics import Color, Rectangle

class HallScreen (Screen):
    def __init__(self, **kwargs):
        super(HallScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)
        
        self.set_window_size()
        self.bg = Image(source='hallscreen.png', keep_ratio=False, allow_stretch=True)
        layout.add_widget(self.bg)

        #Tạo ScrollView cho văn bản
        scroll_view = ScrollView(
            size_hint=(1, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            height = 500,
            do_scroll_x = False,
            do_scroll_y = True
        )
        with scroll_view.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=scroll_view.size, pos=scroll_view.pos)
        
        scroll_view.bind(size=self._update_rect, pos=self._update_rect)

        text = "Text is here"*10
        text_label = Label(
            text = text,
            size_hint_y=None,
            height = scroll_view.height,
            padding = [20, 20, 20, 20],
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size = 20,
            color = (0, 0, 0, 1),
            markup=True,
            halign = 'justify'
        )
        text_label.bind(size=text_label.setter('text_size'))
        text_label.height = text_label.texture_size[1]

        scroll_view.add_widget(text_label)
        layout.add_widget(scroll_view)

        self.backbutton = Button(
            text='Back',
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'left': 1, 'top': 1},
            background_normal='',
            background_color=(0.2, 0.6, 1, 1),
            font_size = 22
        )
        self.backbutton.bind(on_release=self.back_to_menu)
        layout.add_widget(self.backbutton)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def set_window_size(self):
            img = CoreImage('hallscreen.png')
            width, height = img.size
            Window.size = (width*0.35, height*0.35)  
    
    def back_to_menu(self, instance):
        self.manager.current = 'menu'
        self.manager.transition.direction = 'right'

if __name__ == '__main__':
    Window.size = (800, 600)
    class MyApp(App):
        def build(self):
            sm = ScreenManager()
            sm.add_widget(HallScreen(name='hallscreen'))
            return sm
    MyApp().run()