from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from homescreen import HomeScreen
from menuscreen import MenuScreen
from login import LoginImageScreen
class TiNaApp(App):
    def build(self):
        # Tạo ScreenManager để quản lý các màn hình
        screen_manager = ScreenManager()

        # Thêm màn hình HomeScreen
        screen_manager.add_widget(HomeScreen(name='home'))

        # Thêm màn hình MenuScreen
        screen_manager.add_widget(MenuScreen(name='menu'))

        screen_manager.add_widget(LoginImageScreen(name='login_image'))

        return screen_manager

if __name__ == "__main__":
    TiNaApp().run()