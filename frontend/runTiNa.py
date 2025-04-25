from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from homescreen import HomeScreen
from menuscreen import MenuScreen
from login import LoginImageScreen
from hallscreen import HallScreen
from dormitoryscreen import DormitoryScreen
from clusterhallscreen import ClusterHallScreen
from canteenscreen import CanteenScreen
from libraryscreen import LibraryScreen
from ceremonyhallscreen import CeremonyHallScreen
from administrationbuildingscreen import AdministrationBuildingScreen
from sporthallscreen import SportHallScreen
from academicvillagescreen import AcademicVillageScreen
import requests

class TiNaApp(App):
    def build(self):
        self.session = requests.Session()
        # Tạo ScreenManager để quản lý các màn hình
        screen_manager = ScreenManager()

        # Thêm màn hình HomeScreen
        screen_manager.add_widget(HomeScreen(name='home'))

        # Thêm màn hình MenuScreen
        screen_manager.add_widget(MenuScreen(name='menu'))

        screen_manager.add_widget(LoginImageScreen(name='login_image'))
        screen_manager.add_widget(HallScreen(name='lecturehallscreen'))
        screen_manager.add_widget(DormitoryScreen(name='dormitoryscreen'))
        screen_manager.add_widget(ClusterHallScreen(name='clusterhallscreen'))
        screen_manager.add_widget(CanteenScreen(name='canteenscreen'))
        screen_manager.add_widget(LibraryScreen(name='libraryscreen'))
        screen_manager.add_widget(CeremonyHallScreen(name='ceremonyhallscreen'))
        screen_manager.add_widget(AdministrationBuildingScreen(name='administrationbuildingscreen'))
        screen_manager.add_widget(SportHallScreen(name='sporthallscreen'))
        screen_manager.add_widget(AcademicVillageScreen(name='academicvillagescreen'))
        
        return screen_manager

if __name__ == "__main__":
    TiNaApp().run()