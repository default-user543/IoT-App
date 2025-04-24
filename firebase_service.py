from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database.firebase_service import get_all_users, update_user, push_user

class LoginScreen(Screen):
    def login(self):
        username = self.ids.username_input.text.strip()
        password = self.ids.password_input.text.strip()
        if not username or not password:
            self.show_popup("Error", "Please enter both username and password")
            return

        users = get_all_users()
        if users:
            for user_id, user_data in users.items():
                if user_data.get("Username") == username and user_data.get("Password") == password:
                    App.get_running_app().current_user = {
                        "UserID": user_id,
                        "Username": username,
                        "History_of_GPs": user_data.get("History_of_GPs", [])
                    }
                    self.manager.current = "review"
                    return
        self.show_popup("Login Failed", "Invalid username or password")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()


class SignInScreen(Screen):
    def register_user(self):
        username = self.ids.username_input.text.strip()
        password = self.ids.password_input.text.strip()
        forgot_word = self.ids.forgot_word_input.text.strip()

        if not username or not password or not forgot_word:
            self.show_popup("Error", "Please fill all fields")
            return

        users = get_all_users()
        existing_ids = [int(uid) for uid in users.keys() if uid.isdigit()] if users else []
        new_id = str(max(existing_ids) + 1) if existing_ids else "104240001"

        user_data = {
            "Username": username,
            "Password": password,
            "Forgot_Word": forgot_word,
            "History_of_GPs": [],
            "UserID": new_id
        }

        update_user(new_id, user_data)

        App.get_running_app().current_user = {
            "UserID": new_id,
            "Username": username,
            "History_of_GPs": []
        }
        self.manager.current = "review"

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
