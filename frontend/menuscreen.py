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
from kivy.utils import platform
from plyer import gps
import requests
import json


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

        On_text = self.get_username_from_backend()

        # Username
        self.name_label = Label(
            text=f'Hello, {On_text or "Guest"}',
            color=(0.694, 0.875, 0.980, 1),
            halign='left', 
            valign='middle'
        )
        self.name_label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))


        username_box.add_widget(self.name_label)
        header.add_widget(username_box)

        # Share
        share = RelativeLayout(size_hint_x=None, width='30dp', height='30dp')

        share_button = Button(background_normal='', background_down='', background_color=(0, 0, 0, 0))
        share_button.bind(on_press=self.share_location)
        
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

        

        self.mapview = MapView(zoom=17, lat=11.108766932780382, lon=106.61475735229159)  
        marker = MapMarkerPopup(lat=11.108766932780382, lon=106.61475735229159)
        self.mapview.add_widget(marker)

        map_container.add_widget(self.mapview)

        self.loc_getter = LocationGetter(self.mapview)
        self.loc_getter.get_location()

        
        # Scrollable area
        scroll_view = ScrollView(size_hint_y = 1)
        grid_layout = GridLayout(cols=1, size_hint_y=None, spacing=25, padding=(10, 20))
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        # Các khối xanh biển
        items = [
            ("Lecture Hall"),
            ("Sport Hall"),
            ("Canteen"),
            ("Library"),
            ("Dormitory"),
            ("Cluster Hall"),
            ("Ceremony Hall"),
            ("Administration Building"),
            ("Academic Village")
            
        ]


        class StyledButton(ButtonBehavior, BoxLayout):
            def __init__(self, text1, **kwargs):
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
                self.add_widget(self.label1)
            
                

            def update_rect(self, *args):
                self.rect.pos = self.pos
                self.rect.size = self.size

        for item in items:
            btn = StyledButton(text1=item)
            btn.place_name = item  # Gắn tên địa điểm vào button
            btn.bind(on_press=self.go_to_relatedscreen)
            grid_layout.add_widget(btn)

        scroll_view.add_widget(grid_layout)
        main_layout.add_widget(scroll_view)

        self.add_widget(main_layout)

        try:
            gps.configure(on_location=self.on_location, on_status=self.on_status)
            gps.start(minTime=1000, minDistance=1)  # Cập nhật mỗi 1 giây hoặc khi đi được 1m
        except NotImplementedError:
            print("GPS không được hỗ trợ trên thiết bị này")

    
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

    def go_to_relatedscreen(self, instance):
        # Lấy tên nút được nhấn
        place_name = instance.place_name
        screen_name = place_name.replace(' ', '').lower() + 'screen'
        self.manager.current = screen_name

    def share_location(self, instance):
        try:
            response = requests.post("http://127.0.0.1:5000/share")  # hoặc IP backend thực tế
            if response.status_code == 200:
                data = response.json()
                areas = data.get("areas", "Không có dữ liệu khu vực")
                link = data.get("link", "Không có link")
                print("Areas:", areas)
                print("Google Maps link:", link)
                # Optionally: mở link trên trình duyệt
                import webbrowser
                webbrowser.open(link)
            else:
                print("Lỗi khi gọi API:", response.status_code, response.text)
        except Exception as e:
            print("Lỗi kết nối backend:", e)


    def send_location_to_backend(self, latitude, longitude, timestamp):
        url = "http://127.0.0.1:5000/check-location"  
        headers = {'Content-Type': 'application/json'}
        payload = {
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": timestamp
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload), cookies={'session': 'your-session-id'})
            if response.status_code == 200:
                result = response.json()
                zone_name = result.get('name', 'Unknown')
                print(f"You are in: {zone_name}")
                self.update_scrollview_for_location(zone_name)
            else:
                print('Something went wrong')
                self.update_scrollview_for_location("No zone found")
        except Exception as e:
            print(f"Error sending location: {e}")

        

    def on_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        print(f"Vị trí hiện tại: {lat}, {lon}")

        # Thêm marker vào bản đồ
        marker = MapMarkerPopup(lat=lat, lon=lon)
        self.mapview.add_widget(marker)
        self.mapview.center_on(lat, lon)

        from time import time
        self.send_location_to_backend(lat, lon, time())

        # Sau khi gửi lên backend -> lấy kết quả khu vực hiện tại từ backend
        url = "http://127.0.0.1:5000/check-location"
        payload = {
            "latitude": lat,
            "longitude": lon,
            "timestamp": time()
        }
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                result = response.json()
                zone_name = result.get('name', 'Unknown')
                print(f"📍 Đang ở: {zone_name}")

                # Cập nhật giao diện scrollview
                self.update_scrollview_for_location(zone_name)

        except Exception as e:
            print(f"Lỗi lấy zone từ backend: {e}")

    def on_status(self, stype, status):
        print(f"GPS status: {stype} - {status}")


    def get_username_from_backend(self):
        app = App.get_running_app()
        session = app.session
        try:
            res = session.post(
                "http://127.0.0.1:5000/test",  # thay bằng địa chỉ thật
            )
            if res.status_code == 200:    
                data = res.json()
                print(res.json())
                return data.get("username")
            else:
                print("Không thê lấy username", res.status_code)
                return None
        except Exception as e:
            print("Error getting username:", e)
            return None
        
    def on_pre_enter(self):
        username = self.get_username_from_backend()
        if username:
            self.name_label.text = f"Hello, {username}"


    def update_scrollview_for_location(self, current_zone):
        scroll_view = self.children[0].children[0]  # truy cập ScrollView
        grid_layout = scroll_view.children[0]  # truy cập GridLayout

        prioritized_buttons = []
        other_buttons = []

        # Duyệt qua từng button để kiểm tra
        for btn in grid_layout.children[:]:
            if hasattr(btn, 'place_name'):
                if btn.place_name.strip().lower() == current_zone.strip().lower():
                    btn.label1.text = btn.place_name
                    # Thêm label "You are here" nếu chưa có
                    if not hasattr(btn, 'status_label'):
                        status_label = Label(
                            text="You are here",
                            color=(1, 1, 1, 1),
                            font_size='14sp',
                            italic=True,
                            halign='right',
                            valign='middle',
                            size_hint_x=None,
                            padding=(15, 0)
                        )
                        status_label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
                        btn.add_widget(status_label)
                        btn.status_label = status_label
                    prioritized_buttons.append(btn)  
                else:
                    # Ẩn label nếu không phải vị trí hiện tại
                    if hasattr(btn, 'status_label'):
                        btn.remove_widget(btn.status_label)
                        del btn.status_label
                    other_buttons.append(btn)

        # Làm mới lại layout (xóa tất cả → thêm lại theo thứ tự)
        grid_layout.clear_widgets()
        for btn in prioritized_buttons + other_buttons:
            grid_layout.add_widget(btn)
        



class LocationGetter:
    def __init__(self, mapview):
        self.mapview = mapview
        self.location = None
        self.current_marker = None  # Ban đầu chưa có marker

    def get_location(self):
        if platform == 'android':
            self.get_android_location()
        else:
            self.get_ip_location()

    def get_android_location(self):
        try:
            gps.configure(on_location=self.on_location, on_status=self.on_status)
            gps.start(minTime=1000, minDistance=1)
        except NotImplementedError:
            print("GPS không khả dụng trên thiết bị này.")

    def on_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        print(f"📍 Vị trí hiện tại: {lat}, {lon}")

        if self.current_marker:
            self.mapview.remove_widget(self.current_marker)

        self.current_marker = MapMarkerPopup(lat=lat, lon=lon)
        self.mapview.add_widget(self.current_marker)
        self.mapview.center_on(lat, lon)

        from time import time
        self.send_location_to_backend(lat, lon, time())

    def on_status(self, stype, status):
        print("📶 GPS Status:", stype, status)

    def get_ip_location(self):
        
        try:
            res = requests.get("https://ipinfo.io/json")
            data = res.json()
            lat, lon = map(float, data['loc'].split(','))
            print("🌍 IP-based location:", lat, lon)

            if self.current_marker:
                self.mapview.remove_widget(self.current_marker)

            self.current_marker = MapMarkerPopup(lat=lat, lon=lon)
            self.mapview.add_widget(self.current_marker)
            self.mapview.center_on(lat, lon)

            from time import time
            self.send_location_to_backend(lat, lon, time())

        except Exception as e:
            print("Lỗi IP định vị:", e)


