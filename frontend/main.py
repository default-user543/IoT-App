from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

# Set background color for the app
Window.clearcolor = (1, 1, 1, 1)  # White background

# Import screens
from main import MainScreen
from login import LoginImageScreen  # Chỉ import LoginImageScreen
from signin import SignInImageScreen
from forgetpass import ForgetpwImageScreen  # Chỉ import ForgetpwImageScreen
from changepass import ChangepwImageScreen, ChangepwScreen
from homescreen import HomeScreen
from menuscreen import MenuScreen
from places import PlacesScreen
from confirm import ConfirmScreen 
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

# Main application class
class MyApp(App):
    def build(self):
        self.session = requests.Session()    # Store session in the app instance
        # Create ScreenManager to manage screens
        screen_manager = ScreenManager()

        # Add main screen
        screen_manager.add_widget(MainScreen(name='main'))

        # Add login screens
        screen_manager.add_widget(LoginImageScreen(name='login_image'))

        # Add sign-in screens
        screen_manager.add_widget(SignInImageScreen(name='signin_image'))

        # Add forget password screen
        screen_manager.add_widget(ForgetpwImageScreen(name='forget_password_image'))

        # Add change password screens
        screen_manager.add_widget(ChangepwScreen(name='change_password'))
        screen_manager.add_widget(ChangepwImageScreen(name='change_password_image'))

        # Add home and menu screens
        screen_manager.add_widget(HomeScreen(name='home'))
        screen_manager.add_widget(MenuScreen(name='menu'))

        # Add places screen
        screen_manager.add_widget(PlacesScreen(name='places'))

        # Add hall screen
        screen_manager.add_widget(HallScreen(name='lecturehallscreen'))
        screen_manager.add_widget(DormitoryScreen(name='dormitoryscreen'))
        screen_manager.add_widget(ClusterHallScreen(name='clusterhallscreen'))
        screen_manager.add_widget(CanteenScreen(name='canteenscreen'))
        screen_manager.add_widget(LibraryScreen(name='libraryscreen'))
        screen_manager.add_widget(CeremonyHallScreen(name='ceremonyhallscreen'))
        screen_manager.add_widget(AdministrationBuildingScreen(name='administrationbuildingscreen'))
        screen_manager.add_widget(SportHallScreen(name='sporthallscreen'))
        screen_manager.add_widget(AcademicVillageScreen(name='academicvillagescreen'))

        screen_manager.add_widget(ConfirmScreen(name='confirm'))
        return screen_manager

if __name__ == "__main__":
    app = MyApp()
    app.run()
