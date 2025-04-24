[app]

# Tên hiển thị của app
title = IoT App

# Tên gói và domain dùng để tạo package name Android
package.name = iotapp
package.domain = org.defaultuser543

# Thư mục chứa source code
source.dir = .
source.include_exts = py,json,kv,png,jpg

# Phiên bản app
version = 0.1

# Các thư viện Python sẽ được build vào APK
requirements = python3,kivy,requests

# Orientation của app
orientation = portrait

# Có cần fullscreen không
fullscreen = 0

# Nếu app cần internet (Firebase)
android.permissions = INTERNET

# Nếu có dùng location:
# android.permissions = INTERNET,ACCESS_COARSE_LOCATION,ACCESS_FINE_LOCATION

# Nếu dùng các thư viện không có sẵn trên pip
# android.add_source = ...
# android.add_jars = ...

# Mặc định build debug để dễ test
android.debug = 1

# -- Phần bên dưới có thể để nguyên nếu không tuỳ chỉnh build phức tạp --

[buildozer]

log_level = 2
warn_on_root = 1
