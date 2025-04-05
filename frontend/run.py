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

# Main application class
class MyApp(App):
    def build(self):
        # Create ScreenManager to manage screens
        screen_manager = ScreenManager()

        # Add main screen
        main_screen = MainScreen(name='main')
        screen_manager.add_widget(main_screen)

        # Add login screens
        login_image_screen = LoginImageScreen(name='login_image')
        screen_manager.add_widget(login_image_screen)

        # Add sign-in screens
        signin_image_screen = SignInImageScreen(name='signin_image')
        screen_manager.add_widget(signin_image_screen)

        # Add forget password screen
        forgetpw_image_screen = ForgetpwImageScreen(name='forget_password_image')
        screen_manager.add_widget(forgetpw_image_screen)

        # Add change password screens
        changepw_screen = ChangepwScreen(name='change_password')
        screen_manager.add_widget(changepw_screen)

        changepw_image_screen = ChangepwImageScreen(name='change_password_image')
        screen_manager.add_widget(changepw_image_screen)

        return screen_manager

if __name__ == "__main__":
    app = MyApp()
    app.run()