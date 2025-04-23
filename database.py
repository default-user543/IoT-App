import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import requests
import datetime

# Firebase URLs (mỗi mục dùng domain riêng theo yêu cầu)
USERS_URL = "https://app-du-lich-4d8a4.asia-southeast1.firebasedatabase.app/users.json"
REVIEWS_URL = "https://app-du-lich-4d8a4.asia-southeast1.firebasedatabase.app/reviews.json"

class LoginScreen(Screen):
    def login(self):
        email = self.ids.email_input.text.strip().lower()
        if not email:
            self.show_popup("Error", "Please enter your email")
            return

        try:
            response = requests.get(USERS_URL)
            if response.status_code == 200:
                users = response.json()
                if isinstance(users, dict):
                    for user_id, user_data in users.items():
                        if user_data.get("E-Mail", "").lower() == email:
                            App.get_running_app().current_user = {
                                "UserID": user_id,
                                "Name": user_data.get("Name", "User")
                            }
                            self.manager.current = "review"
                            return
                elif isinstance(users, list):
                    for user_data in users:
                        if user_data.get("E-Mail", "").lower() == email:
                            App.get_running_app().current_user = {
                                "UserID": user_data.get("UserID", ""),
                                "Name": user_data.get("Name", "User")
                            }
                            self.manager.current = "review"
                            return
            self.show_popup("Login Failed", "Email not found. Please sign in first.")
        except Exception as e:
            self.show_popup("Login Error", f"Something went wrong: {e}")

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class SignInScreen(Screen):
    def register_user(self):
        email = self.ids.email_input.text.strip().lower()
        name = self.ids.name_input.text.strip()
        age = self.ids.age_input.text.strip()
        gender = self.ids.gender_spinner.text

        if not email or not name or not age or gender == "Select Gender":
            self.show_popup("Error", "Please fill all fields")
            return

        response = requests.get(USERS_URL)
        if response.status_code == 200:
            users = response.json() or {}
            existing_ids = [int(uid) for uid in users.keys() if uid.isdigit()]
            new_id = str(max(existing_ids) + 1) if existing_ids else "104240001"

            user_data = {
                "E-Mail": email,
                "Name": name,
                "Age": age,
                "Gender": gender,
                "UserID": new_id
            }

            requests.patch(f"https://app-du-lich-4d8a4.asia-southeast1.firebasedatabase.app/users/{new_id}.json", json=user_data)
            App.get_running_app().current_user = {"UserID": new_id, "Name": name}
            self.manager.current = "review"

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class ReviewScreen(Screen):
    def on_enter(self):
        self.load_zones()
        self.display_welcome()
        self.load_reviews()

    def display_welcome(self):
        user = App.get_running_app().current_user
        name = user.get("Name", "User")
        self.ids.welcome_label.text = f"Welcome {name}!"

    def load_zones(self):
        # Danh sách các zone sẽ được hiển thị trên Spinner
        zone_names = [
            "academic_cluster_1",
            "academic_cluster_2",
            "academic_cluster_5",
            "academic_cluster_6",
            "admin_building",
            "ceremoney_hall",
            "dorm_1",
            "dorm_2",
            "lecture_hall",
            "library",
            "sports_hall",
            "university_guest_house"
        ]
        
        # Cập nhật các zone vào spinner
        self.ids.zone_spinner.values = zone_names
        if zone_names:
            self.ids.zone_spinner.text = zone_names[0]  # Chọn zone đầu tiên mặc định

    def load_reviews(self):
        user = App.get_running_app().current_user
        response = requests.get(REVIEWS_URL)
        if response.status_code == 200:
            all_reviews = response.json() or {}
            user_reviews = [
                {"key": key, **review} for key, review in all_reviews.items()
                if review.get("UserID") == user["UserID"]
            ]
            self.display_reviews(user_reviews)

    def display_reviews(self, reviews):
        container = self.ids.reviews_container
        container.clear_widgets()
        for review in reviews:
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            box.add_widget(Label(text=review.get("Zone"), size_hint_x=0.3))
            box.add_widget(Label(text=review.get("Content"), size_hint_x=0.4))
            edit_btn = Button(text="Edit", size_hint_x=0.15)
            delete_btn = Button(text="Delete", size_hint_x=0.15)
            edit_btn.bind(on_release=lambda btn, r=review: self.edit_review(r))
            delete_btn.bind(on_release=lambda btn, r=review: self.delete_review(r))
            box.add_widget(edit_btn)
            box.add_widget(delete_btn)
            container.add_widget(box)

    def submit_review(self):
        content = self.ids.review_input.text.strip()
        zone = self.ids.zone_spinner.text
        if not content or zone == "Select Zone":
            self.show_popup("Error", "Please write review and select zone")
            return
        user = App.get_running_app().current_user
        review_data = {
            "UserID": user["UserID"],
            "Content": content,
            "Zone": zone,
            "Time": datetime.datetime.now().isoformat()
        }
        requests.post(REVIEWS_URL, json=review_data)
        self.ids.review_input.text = ""
        self.load_reviews()

    def edit_review(self, review):
        self.ids.review_input.text = review["Content"]
        self.ids.zone_spinner.text = review["Zone"]
        self.current_edit_key = review["key"]

    def delete_review(self, review):
        key = review["key"]
        requests.delete(f"https://app-du-lich-4d8a4.asia-southeast1.firebasedatabase.app/reviews/{key}.json")
        self.load_reviews()

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class ReviewApp(App):
    current_user = {}

    def build(self):
        self.title = "Review App"
        Builder.load_file("screens/reviews.kv")
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignInScreen(name="signin"))
        sm.add_widget(ReviewScreen(name="review"))
        return sm

if __name__ == '__main__':
    ReviewApp().run()


# Embedded zone data from JSON
ZONE_DATA = {
  "zones": {
    "academic_cluster_1": {
      "name": "Academic Cluster 1",
      "polygon": [
        {
          "lat": 11.108766932780382,
          "lng": 106.61475735229159
        },
        {
          "lat": 11.108277522709393,
          "lng": 106.614941891544
        },
        {
          "lat": 11.108520596480586,
          "lng": 106.61550049684865
        },
        {
          "lat": 11.109013268872221,
          "lng": 106.61532593269095
        }
      ]
    },
    "academic_cluster_2": {
      "name": "Academic Cluster 2",
      "polygon": [
        {
          "lat": 11.108233285717834,
          "lng": 106.61497410224997
        },
        {
          "lat": 11.107843384968529,
          "lng": 106.61510576678295
        },
        {
          "lat": 11.108053331590593,
          "lng": 106.61566063874334
        },
        {
          "lat": 11.108447846262996,
          "lng": 106.61552897421036
        }
      ]
    },
    "academic_cluster_5": {
      "name": "Academic Cluster 5",
      "polygon": [
        {
          "lat": 11.109020006958495,
          "lng": 106.61541376774471
        },
        {
          "lat": 11.108417853951245,
          "lng": 106.61566534104878
        },
        {
          "lat": 11.108630107260351,
          "lng": 106.61624607568527
        },
        {
          "lat": 11.109269173356648,
          "lng": 106.61601801390495
        }
      ]
    },
    "academic_cluster_6": {
      "name": "Academic Cluster 6",
      "polygon": [
        {
          "lat": 11.108325569839131,
          "lng": 106.61568179911791
        },
        {
          "lat": 11.107741872258465,
          "lng": 106.61591221205062
        },
        {
          "lat": 11.10796104737623,
          "lng": 106.61647883977287
        },
        {
          "lat": 11.108549358720522,
          "lng": 106.61627664066866
        }
      ]
    },
    "admin_building": {
      "name": "Admin Building",
      "polygon": [
        {
          "lat": 11.10980589340776,
          "lng": 106.61435949231425
        },
        {
          "lat": 11.109358684783043,
          "lng": 106.6145188647208
        },
        {
          "lat": 11.109811380625883,
          "lng": 106.61575749588035
        },
        {
          "lat": 11.11030522983522,
          "lng": 106.6156148995166
        }
      ]
    },
    "ceremoney_hall": {
      "name": "Ceremony Hall",
      "polygon": [
        {
          "lat": 11.108042232288632,
          "lng": 106.6129853108017
        },
        {
          "lat": 11.1077599568676,
          "lng": 106.61307032505268
        },
        {
          "lat": 11.108026711997663,
          "lng": 106.61388685727688
        },
        {
          "lat": 11.108351667917553,
          "lng": 106.61374450783345
        }
      ]
    },
    "dorm_1": {
      "name": "Dorm 1",
      "polygon": [
        {
          "lat": 11.107783774691464,
          "lng": 106.61207810676271
        },
        {
          "lat": 11.107191586406204,
          "lng": 106.61230254639403
        },
        {
          "lat": 11.10741182185925,
          "lng": 106.61292100226702
        },
        {
          "lat": 11.10805947626555,
          "lng": 106.61270820024622
        }
      ]
    },
    "dorm_2": {
      "name": "Dorm 2",
      "polygon": [
        {
          "lat": 11.106614079294477,
          "lng": 106.61250869835385
        },
        {
          "lat": 11.106003943445598,
          "lng": 106.61274810062724
        },
        {
          "lat": 11.106240493591871,
          "lng": 106.61335325637395
        },
        {
          "lat": 11.106840840688609,
          "lng": 106.61315209196364
        }
      ]
    },
    "lecture_hall": {
      "name": "Lecture Hall",
      "polygon": [
        {
          "lat": 11.107111000874026,
          "lng": 106.61433409957904
        },
        {
          "lat": 11.106600769247835,
          "lng": 106.61452587591256
        },
        {
          "lat": 11.106936396995874,
          "lng": 106.61543137653894
        },
        {
          "lat": 11.107446628035303,
          "lng": 106.61524750850782
        }
      ]
    },
    "library": {
      "name": "Library",
      "polygon": [
        {
          "lat": 11.108388528571519,
          "lng": 106.61382062524984
        },
        {
          "lat": 11.108032532109064,
          "lng": 106.61391651341684
        },
        {
          "lat": 11.108308987165445,
          "lng": 106.61471129781462
        },
        {
          "lat": 11.108616482485534,
          "lng": 106.61461540964787
        }
      ]
    },
    "sports_hall": {
      "name": "Sports Hall",
      "polygon": [
        {
          "lat": 11.106135424993408,
          "lng": 106.61355345648064
        },
        {
          "lat": 11.105009548228654,
          "lng": 106.61384970167983
        },
        {
          "lat": 11.10476960671742,
          "lng": 106.61539675994226
        },
        {
          "lat": 11.105171047211694,
          "lng": 106.61589520424566
        },
        {
          "lat": 11.10681371750534,
          "lng": 106.61545318759926
        }
      ]
    },
    "university_guest_house": {
      "name": "University Guest House",
      "polygon": [
        {
          "lat": 11.109462969306996,
          "lng": 106.61648354209245
        },
        {
          "lat": 11.10828865621168,
          "lng": 106.61706897903385
        },
        {
          "lat": 11.109430669984969,
          "lng": 106.61875710643875
        },
        {
          "lat": 11.110152789535334,
          "lng": 106.61841618934763
        }
      ]
    }
  }
}

GOOGLE_MAPS_API_KEY = "AIzaSyA_AtjVapEMZKN4SUjmD5yD5z6sEsaLylA"



